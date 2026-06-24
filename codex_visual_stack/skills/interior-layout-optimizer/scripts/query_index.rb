#!/usr/bin/env ruby
# frozen_string_literal: true
# encoding: UTF-8

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

require 'json'
require 'digest/sha1'
require 'optparse'

DEFAULT_INDEX = File.expand_path('../assets/index', __dir__)
SEM_DIMS = 128
VIS_DIMS = 32

options = {
  index: DEFAULT_INDEX,
  query: nil,
  limit: 8,
  scope: 'cases',
  quality: nil,
  role: nil,
  typology: nil,
  area_min: nil,
  area_max: nil,
  rooms: nil,
  json: false
}

OptionParser.new do |opts|
  opts.banner = 'Usage: query_index.rb --query TEXT [--scope cases|assets|both] [filters]'
  opts.on('--index DIR', 'Index directory') { |v| options[:index] = v }
  opts.on('-q', '--query TEXT', 'Natural-language retrieval query') { |v| options[:query] = v }
  opts.on('-n', '--limit N', Integer, 'Number of results') { |v| options[:limit] = v }
  opts.on('--scope SCOPE', 'cases, assets, or both') { |v| options[:scope] = v }
  opts.on('--quality SIGNAL', 'positive, negative, neutral, ignore') { |v| options[:quality] = v }
  opts.on('--role ROLE', '文件角色过滤，如 优秀案例/反例/原始/建筑图/主讲/推导方案') { |v| options[:role] = v }
  opts.on('--typology TYPE', '户型类型过滤，如 平层/复式/别墅/大平层/异型平层') { |v| options[:typology] = v }
  opts.on('--area-min N', Float, 'Minimum area') { |v| options[:area_min] = v }
  opts.on('--area-max N', Float, 'Maximum area') { |v| options[:area_max] = v }
  opts.on('--rooms N', Integer, 'Bedroom/room count after +1 expansion') { |v| options[:rooms] = v }
  opts.on('--json', 'Emit JSON') { options[:json] = true }
end.parse!

query = (options[:query] || ARGV.join(' ')).to_s
abort 'Provide --query TEXT' if query.strip.empty?

def fs_text(s)
  s.to_s.dup.force_encoding('UTF-8')
end

def normalize_text(s)
  fs_text(s).unicode_normalize(:nfkc)
rescue StandardError
  fs_text(s)
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
  vec.map { |x| x / mag }
end

def query_vector(text)
  t = normalize_text(text)
  vec = Array.new(SEM_DIMS, 0.0)
  add_hash_vec(vec, t, 1.0)
  # Expand common design intents so natural-language queries find filename-derived source vectors.
  expansions = []
  expansions << '小户型 一居 收纳 复合 客餐厨一体' if t.match?(/小户型|单身|公寓|一居|studio|收纳|紧凑/)
  expansions << '紧凑 二居 一居改两居 收纳' if t.match?(/两居|二居|改两房|改二房|二房/)
  expansions << '中小户型 二加一 三房 公私分区' if t.match?(/2\+1|二加一|三房|3房|三居|书房|多功能房/)
  expansions << '改善型 三房 四房 家政 中西厨 套房' if t.match?(/改善|四房|4房|家政|中西厨|套房/)
  expansions << '大宅 大平层 套房 洄游 双餐厨' if t.match?(/大宅|大平层|洄游|横厅|社交|双餐厨/)
  expansions << '豪宅 别墅 多套房 多动线 家政 储藏' if t.match?(/别墅|豪宅|多层|庭院|地下|车库/)
  expansions << '楼梯 上下层 动静分区 挑空' if t.match?(/复式|loft|楼梯|上下层|挑空/)
  expansions << '异形 斜墙 不规则 动线校正' if t.match?(/异型|异形|斜墙|不规则/)
  expansions << '优秀案例 positive' if t.match?(/优秀|正例|参考|好方案/)
  expansions << '反例 negative' if t.match?(/反例|避坑|错误|问题/)
  expansions.each { |e| add_hash_vec(vec, e, 1.9) }
  sem = norm(vec)
  sem.map { |x| x * 0.86 } + Array.new(VIS_DIMS, 0.0)
end

def cosine(a, b)
  n = [a.length, b.length].min
  s = 0.0
  n.times { |i| s += a[i].to_f * b[i].to_f }
  s
end

def read_jsonl(path)
  File.readlines(path, encoding: 'UTF-8').map { |line| JSON.parse(line) }
end

def filter_rows(rows, options)
  rows.select do |r|
    if options[:quality]
      if r.key?('quality_signal')
        next false if r['quality_signal'] != options[:quality]
      elsif options[:quality] == 'positive'
        next false unless r.dig('by_role', '优秀案例').to_i.positive?
      elsif options[:quality] == 'negative'
        next false unless r.dig('by_role', '反例').to_i.positive?
      end
    end
    if options[:role]
      if r.key?('file_role')
        next false if r['file_role'] != options[:role]
      else
        next false unless r.dig('by_role', options[:role]).to_i.positive?
      end
    end
    next false if options[:typology] && r['typology'] != normalize_text(options[:typology])
    next false if options[:area_min] && (!r['area_m2'] || r['area_m2'] < options[:area_min])
    next false if options[:area_max] && (!r['area_m2'] || r['area_m2'] > options[:area_max])
    next false if options[:rooms] && r['bedroom_count'] != options[:rooms]
    true
  end
end

qv = norm(query_vector(query))
query_norm = normalize_text(query)
outputs = {}
if %w[cases both].include?(options[:scope])
  rows = filter_rows(read_jsonl(File.join(options[:index], 'cases.jsonl')), options)
  outputs['cases'] = rows.map do |r|
    bonus = 0.0
    bonus += 0.12 if r['area_m2'] && query_norm.include?(r['area_m2'].round.to_s)
    bonus += 0.08 if r['case_name'] && query_norm.include?(normalize_text(r['case_name']).split(/[（(]/).first.to_s)
    bonus += 0.05 if r['bedroom_count'] && query_norm.match?(/#{r['bedroom_count']}房|#{r['bedroom_count']}室/)
    bonus += 0.06 if query_norm.match?(/反例|负面|避坑/) && r.dig('by_role', '反例').to_i.positive?
    bonus += 0.06 if query_norm.match?(/优秀|正例|参考/) && r.dig('by_role', '优秀案例').to_i.positive?
    r.merge('_score' => cosine(qv, r['vector']) + bonus)
  end.sort_by { |r| -r['_score'] }.first(options[:limit])
end
if %w[assets both].include?(options[:scope])
  rows = filter_rows(read_jsonl(File.join(options[:index], 'assets.jsonl')), options)
  outputs['assets'] = rows.map do |r|
    bonus = 0.0
    bonus += 0.12 if r['area_m2'] && query_norm.include?(r['area_m2'].round.to_s)
    bonus += 0.08 if r['case_name'] && query_norm.include?(normalize_text(r['case_name']).split(/[（(]/).first.to_s)
    bonus += 0.05 if r['bedroom_count'] && query_norm.match?(/#{r['bedroom_count']}房|#{r['bedroom_count']}室/)
    bonus += 0.06 if query_norm.match?(/反例|负面|避坑/) && r['quality_signal'] == 'negative'
    bonus += 0.06 if query_norm.match?(/优秀|正例|参考/) && r['quality_signal'] == 'positive'
    r.merge('_score' => cosine(qv, r['vector']) + bonus)
  end.sort_by { |r| -r['_score'] }.first(options[:limit])
end

if options[:json]
  puts JSON.pretty_generate(outputs)
  exit
end

puts "# Interior layout source retrieval"
puts "Query: #{query}"
puts
if outputs['cases']
  puts "## Top cases"
  outputs['cases'].each_with_index do |r, i|
    puts "#{i + 1}. #{r['case_name']}  score=#{format('%.3f', r['_score'])}"
    puts "   - type=#{r['typology']} area=#{r['area_m2'] || 'n/a'}㎡ rooms=#{r['bedroom_count'] || 'n/a'} assets=#{r['asset_count']}"
    puts "   - source=#{r['path']}"
    reps = (r['representative_assets'] || []).first(3).map { |a| "#{a['file_name']}〔#{a['file_role']}〕" }.join('；')
    puts "   - reps=#{reps}" unless reps.empty?
  end
  puts
end
if outputs['assets']
  puts "## Top source assets"
  outputs['assets'].each_with_index do |r, i|
    puts "#{i + 1}. #{r['case_name']} / #{r['file_name']}  score=#{format('%.3f', r['_score'])}"
    puts "   - role=#{r['file_role']} quality=#{r['quality_signal']} type=#{r['typology']} area=#{r['area_m2'] || 'n/a'}㎡ rooms=#{r['bedroom_count'] || 'n/a'}"
    puts "   - source=#{r['path']}"
  end
end
