#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: UTF-8
Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

require 'json'
require 'digest/sha1'
require 'fileutils'
require 'optparse'
require 'time'

DEFAULT_SOURCE = '/Volumes/homes/saboo内部学习资料/SC071—135个通用户型平面布局优化方案2000+'
DEFAULT_OUT = File.expand_path('../assets/index', __dir__)
IMG_EXTS = %w[.jpg .jpeg .png .webp .tif .tiff].freeze
SKIP_NAMES = ['.DS_Store', 'Thumbs.db'].freeze
SEM_DIMS = 128
VIS_DIMS = 32

options = { source: DEFAULT_SOURCE, out: DEFAULT_OUT }
OptionParser.new do |opts|
  opts.banner = 'Usage: build_index.rb [--source PATH] [--out DIR]'
  opts.on('--source PATH', 'Asset library root') { |v| options[:source] = v }
  opts.on('--out DIR', 'Index output directory') { |v| options[:out] = v }
end.parse!

source = options[:source].to_s.dup.force_encoding('UTF-8')
out = options[:out].to_s.dup.force_encoding('UTF-8')
raise "Source does not exist: #{source}" unless Dir.exist?(source)

FileUtils.mkdir_p(out)

def fs_text(s)
  s.to_s.dup.force_encoding('UTF-8')
end

def normalize_text(s)
  fs_text(s).unicode_normalize(:nfkc)
rescue StandardError
  fs_text(s)
end

def safe_id(s)
  normalize_text(s).gsub(%r{[\s/\\:：()（）+㎡—–]+}, '-').gsub(/^-+|-+$/, '')[0, 80]
end

def parse_case(name)
  raw = fs_text(name)
  n = normalize_text(raw)
  # NFKC turns "㎡" into "m2"; add a separator after area units so room regexes do not read "95㎡3房" as "23房".
  room_n = n.gsub(/([0-9]+(?:\.[0-9]+)?)\s*(?:㎡|m²|m2|m虏|m)/i, '\1㎡ ')
  area = n[/([0-9]+(?:\.[0-9]+)?)\s*(?:㎡|m²|m2|m虏|m)/i, 1]&.to_f
  solution_count = n[/[（(]([0-9]+)\s*稿方案[）)]/, 1]&.to_i
  typology = if n.include?('复式')
               '复式'
             elsif n.match?(/别墅|小别墅|双拼/)
               '别墅'
             elsif n.include?('大平层')
               '大平层'
             elsif n.include?('异型')
               '异型平层'
             elsif n.include?('平层')
               '平层'
             else
               '未标注'
             end
  rooms = nil
  plus_room = false
  if (m = room_n.match(/([0-9]+)\s*\+\s*([0-9]+)房/))
    rooms = m[1].to_i + m[2].to_i
    plus_room = true
  elsif (m = room_n.match(/([0-9]+)房/))
    rooms = m[1].to_i
  elsif room_n.include?('一居室')
    rooms = 1
  elsif room_n.match?(/两居室|二居室/)
    rooms = 2
  elsif room_n.include?('三居室')
    rooms = 3
  elsif room_n.include?('四居室')
    rooms = 4
  end
  area_bucket = if area.nil?
                  '未标注'
                elsif area < 50
                  'S<50'
                elsif area < 80
                  'S50-79'
                elsif area < 120
                  'M80-119'
                elsif area < 160
                  'L120-159'
                elsif area < 220
                  'XL160-219'
                elsif area < 400
                  'XXL220-399'
                else
                  'Estate400+'
                end
  { 'case_name' => name, 'case_id' => safe_id(name), 'area_m2' => area,
    'solution_count' => solution_count, 'typology' => typology,
    'bedroom_count' => rooms, 'plus_room' => plus_room,
    'area_bucket' => area_bucket }
end

def classify_file(name)
  n = normalize_text(name)
  role = '方案'
  quality = 'neutral'
  sequence = n[/^|[^0-9]([0-9]{1,4})(?=[^0-9]|$)/, 1]&.to_i
  role = '原始/建筑图' if n.match?(/原始|建筑|平面图|户型|毛坯|CAD|图框/)
  role = '主讲/推导方案' if n.match?(/曹方案|方案[0-9]|平面方案|投稿平面方案/)
  if n.match?(/优秀|优秀案例|优秀学员/)
    role = '优秀案例'
    quality = 'positive'
  end
  if n.match?(/反例|反面|失败|差/)
    role = '反例'
    quality = 'negative'
  end
  role = '其他案例' if n.match?(/其他案例|其他/)
  if n.match?(/微信|关注|好评|设计行/)
    role = '广告/无关'
    quality = 'ignore'
  end
  { 'file_role' => role, 'quality_signal' => quality, 'sequence' => sequence }
end

def png_dimensions(path)
  File.open(path, 'rb') do |f|
    sig = f.read(24)
    return nil unless sig && sig.bytesize >= 24 && sig.start_with?("\x89PNG".b)
    return sig[16, 8].unpack('NN')
  end
rescue StandardError
  nil
end

def jpeg_dimensions(path)
  File.open(path, 'rb') do |f|
    return nil unless f.read(2) == "\xFF\xD8".b
    loop do
      b = f.read(1)
      return nil unless b
      next unless b == "\xFF".b
      marker = f.read(1)
      marker = f.read(1) while marker == "\xFF".b
      return nil unless marker
      code = marker.ord
      next if code == 0xD8 || code == 0xD9
      len_data = f.read(2)
      return nil unless len_data && len_data.bytesize == 2
      len = len_data.unpack1('n')
      return nil if len < 2
      if [0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF].include?(code)
        data = f.read(5)
        return nil unless data && data.bytesize == 5
        h, w = data[1, 4].unpack('nn')
        return [w, h]
      end
      f.seek(len - 2, IO::SEEK_CUR)
    end
  end
rescue StandardError
  nil
end

def image_dimensions(path, ext)
  case ext
  when '.png' then png_dimensions(path)
  when '.jpg', '.jpeg' then jpeg_dimensions(path)
  else nil
  end
end

def add_hash_vec(vec, token, weight)
  normalize_text(token).downcase.split(/[\s_\-、，,。\.\/\\:：;；（）()\[\]{}]+/).reject(&:empty?).each do |part|
    bytes = Digest::SHA1.digest(part).bytes
    vec[bytes[0] % vec.length] += (bytes[1].odd? ? 1.0 : -1.0) * weight
    chars = part.each_char.to_a
    next unless chars.length > 1
    chars.each_cons(2) do |a, b|
      h = Digest::SHA1.digest(a + b).bytes
      vec[h[0] % vec.length] += (h[1].odd? ? 1.0 : -1.0) * weight * 0.35
    end
  end
end

def norm(vec)
  mag = Math.sqrt(vec.sum { |x| x * x })
  return Array.new(vec.length, 0.0) if mag.zero?
  vec.map { |x| (x / mag).round(6) }
end

def semantic_tokens(rec)
  toks = []
  add = ->(text, w = 1.0) { toks << [text.to_s, w] unless text.nil? || text.to_s.empty? }
  add.call(rec['case_name'], 1.0)
  add.call(rec['file_name'], 0.8)
  add.call(rec['typology'], 2.0)
  add.call(rec['area_bucket'], 1.6)
  add.call(rec['file_role'], 1.6)
  add.call(rec['quality_signal'], 1.5)
  if rec['area_m2']
    area = rec['area_m2'].round
    add.call("#{area}㎡", 1.8)
    add.call("面积#{area}", 1.2)
  end
  if rec['bedroom_count']
    add.call("#{rec['bedroom_count']}房", 2.0)
    add.call("卧室#{rec['bedroom_count']}", 1.0)
  end
  add.call('加一 多功能房 书房 +1', 2.0) if rec['plus_room']
  add.call('异形 斜墙 不规则 动线校正', 2.0) if rec['typology'].include?('异型')
  add.call('楼梯 上下层 动静分区 挑空', 2.0) if rec['typology'].include?('复式')
  add.call('别墅 多层 套房 中西厨 家政', 2.0) if rec['typology'].include?('别墅')
  add.call('大平层 横厅 洄游 套房 社交', 1.8) if rec['typology'].include?('大平层')
  if rec['area_m2']
    a = rec['area_m2']
    phrase = if a < 50
               '小户型 一居 收纳 复合 客餐厨一体'
             elsif a < 80
               '紧凑 二居 一居改两居 收纳'
             elsif a < 120
               '中小户型 二加一 三房 公私分区'
             elsif a < 160
               '改善型 三房 四房 家政 中西厨 套房'
             elsif a < 220
               '大宅 大平层 套房 洄游 双餐厨'
             else
               '豪宅 别墅 多套房 多动线 家政 储藏'
             end
    add.call(phrase, 1.8)
  end
  toks
end

def semantic_vector(rec)
  vec = Array.new(SEM_DIMS, 0.0)
  semantic_tokens(rec).each { |t, w| add_hash_vec(vec, t, w) }
  norm(vec)
end

def visual_vector(rec)
  vec = Array.new(VIS_DIMS, 0.0)
  w = rec['width'].to_f
  h = rec['height'].to_f
  bytes = rec['bytes'].to_f
  ext = rec['ext'].to_s
  features = [
    w.positive? && h.positive? ? [w / h, 4.0].min / 4.0 : 0.0,
    w.positive? && h.positive? ? [h / w, 4.0].min / 4.0 : 0.0,
    w.positive? && h.positive? ? Math.log10([w * h, 1].max) / 8.0 : 0.0,
    bytes.positive? ? Math.log10(bytes) / 8.0 : 0.0,
    ext == '.png' ? 1.0 : 0.0,
    ext == '.jpg' || ext == '.jpeg' ? 1.0 : 0.0
  ]
  features.each_with_index { |v, i| vec[i] = v }
  add_hash_vec(vec, rec['file_name'], 0.35)
  norm(vec)
end

def combine_vectors(sem, vis)
  norm(sem.map { |x| x * 0.86 } + vis.map { |x| x * 0.14 })
end

def cosine(a, b)
  n = [a.length, b.length].min
  s = 0.0
  n.times { |i| s += a[i].to_f * b[i].to_f }
  s
end

def jsonl_write(path, rows)
  File.open(path, 'w:utf-8') { |f| rows.each { |row| f.puts(JSON.generate(row)) } }
end

case_dirs = Dir.children(source).map { |name| fs_text(name) }.select do |name|
  full = File.join(source, name)
  File.directory?(full) && !name.start_with?('.')
end.sort

assets = []
cases = []
asset_seq = 0
case_dirs.each_with_index do |dirname, idx|
  case_path = File.join(source, dirname)
  cmeta = parse_case(dirname)
  files = Dir.children(case_path).map { |name| fs_text(name) }.select do |name|
    full = File.join(case_path, name)
    File.file?(full) && !name.start_with?('._') && !SKIP_NAMES.include?(name)
  end.sort
  case_assets = []
  files.each do |fname|
    full = File.join(case_path, fname)
    ext = File.extname(fname).downcase
    width = height = nil
    if IMG_EXTS.include?(ext)
      dims = image_dimensions(full, ext)
      width, height = dims if dims
    end
    asset_seq += 1
    rec = {
      'id' => format('asset-%04d', asset_seq),
      'path' => full,
      'smb_url' => "smb://SABOO_STUDIO1._smb._tcp.local/homes/saboo内部学习资料/SC071—135个通用户型平面布局优化方案2000+/#{dirname}/#{fname}",
      'case_id' => cmeta['case_id'],
      'case_name' => dirname,
      'file_name' => fname,
      'ext' => ext,
      'bytes' => File.size(full),
      'width' => width,
      'height' => height
    }.merge(cmeta).merge(classify_file(fname))
    rec['semantic_vector'] = semantic_vector(rec)
    rec['visual_vector'] = visual_vector(rec)
    rec['vector'] = combine_vectors(rec['semantic_vector'], rec['visual_vector'])
    assets << rec
    case_assets << rec
  end
  sem = Array.new(SEM_DIMS, 0.0)
  vis = Array.new(VIS_DIMS, 0.0)
  combined = Array.new(SEM_DIMS + VIS_DIMS, 0.0)
  case_assets.each do |a|
    a['semantic_vector'].each_with_index { |v, i| sem[i] += v }
    a['visual_vector'].each_with_index { |v, i| vis[i] += v }
    a['vector'].each_with_index { |v, i| combined[i] += v }
  end
  by_role = case_assets.group_by { |a| a['file_role'] }.transform_values(&:length)
  by_ext = case_assets.group_by { |a| a['ext'] }.transform_values(&:length)
  score = lambda do |a|
    s = 0.0
    s += 4 if a['quality_signal'] == 'positive'
    s += 3 if a['file_role'] == '主讲/推导方案'
    s += 2 if a['file_role'] == '原始/建筑图'
    s += 1 if IMG_EXTS.include?(a['ext'])
    s += 0.3 if a['ext'] == '.png'
    s -= 10 if a['file_role'] == '广告/无关'
    s
  end
  reps = case_assets.sort_by { |a| [-score.call(a), a['sequence'] || 9999, a['file_name']] }.first(10).map do |a|
    a.slice('id', 'file_name', 'path', 'file_role', 'quality_signal', 'width', 'height')
  end
  cases << {
    'case_id' => cmeta['case_id'],
    'case_name' => dirname,
    'path' => case_path,
    'smb_url' => "smb://SABOO_STUDIO1._smb._tcp.local/homes/saboo内部学习资料/SC071—135个通用户型平面布局优化方案2000+/#{dirname}"
  }.merge(cmeta).merge(
    'asset_count' => case_assets.length,
    'image_count' => case_assets.count { |a| IMG_EXTS.include?(a['ext']) },
    'by_role' => by_role,
    'by_ext' => by_ext,
    'representative_assets' => reps,
    'semantic_vector' => norm(sem),
    'visual_vector' => norm(vis),
    'vector' => norm(combined)
  )
  warn "indexed #{idx + 1}/#{case_dirs.length} cases, #{assets.length} assets" if ((idx + 1) % 25).zero?
end

jsonl_write(File.join(out, 'assets.jsonl'), assets)
jsonl_write(File.join(out, 'cases.jsonl'), cases)
manifest = {
  'source_root' => source,
  'source_smb' => 'smb://SABOO_STUDIO1._smb._tcp.local/homes/saboo内部学习资料/SC071—135个通用户型平面布局优化方案2000+',
  'built_at' => Time.now.utc.iso8601,
  'case_count' => cases.length,
  'asset_count' => assets.length,
  'image_count' => assets.count { |a| IMG_EXTS.include?(a['ext']) },
  'dimensions' => { 'semantic' => SEM_DIMS, 'visual' => VIS_DIMS, 'combined' => SEM_DIMS + VIS_DIMS },
  'extensions' => assets.group_by { |a| a['ext'] }.transform_values(&:length).sort.to_h,
  'typologies' => cases.group_by { |c| c['typology'] }.transform_values(&:length).sort.to_h,
  'area_buckets' => cases.group_by { |c| c['area_bucket'] }.transform_values(&:length).sort.to_h,
  'quality_assets' => assets.group_by { |a| a['quality_signal'] }.transform_values(&:length).sort.to_h,
  'role_assets' => assets.group_by { |a| a['file_role'] }.transform_values(&:length).sort.to_h,
  'notes' => 'Vectors are deterministic local feature vectors combining Chinese/English metadata, case typology, area/room signals, source filename roles, and lightweight image geometry. They cite each source asset by local path and SMB URL.'
}
File.write(File.join(out, 'manifest.json'), JSON.pretty_generate(manifest), mode: 'w:utf-8')
puts JSON.pretty_generate(manifest)
