# AppleScript-safe Patterns

## 1. Absolute runtime paths

Use absolute paths. `do shell script` has a reduced environment.

```applescript
set py to "/Users/bonnie/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
```

## 2. Quoted command builder

```applescript
set cmd to quoted form of py & " " & quoted form of scriptPath & " " & quoted form of inputPath
set resultText to do shell script cmd
```

## 3. Multiple args

```applescript
set cmd to quoted form of py & " " & quoted form of scriptPath & " " & quoted form of inputPath & " " & quoted form of outputPath & " 2400 1600"
do shell script cmd
```

## 4. Open or reveal result

```applescript
tell application "Finder"
  reveal POSIX file outputPath
  activate
end tell
```

## 5. Run SketchUp socket bridge

```applescript
set py to "/Users/bonnie/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
set bridge to "/Users/bonnie/Documents/设计项目/廖哥雅居_室内设计总控/scripts/sketchup_socket_bridge.py"
set rb to "/Users/bonnie/Documents/设计项目/廖哥雅居_室内设计总控/03_SketchUp_Model/LIAO_R02_precise_white_model_from_CAD_ref.rb"

set cmd to quoted form of py & " " & quoted form of bridge & " load " & quoted form of rb & " --timeout 240"
do shell script cmd
```

## 6. Export SketchUp scenes

```applescript
set py to "/Users/bonnie/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
set bridge to "/Users/bonnie/Documents/设计项目/廖哥雅居_室内设计总控/scripts/sketchup_socket_bridge.py"
set outDir to "/Users/bonnie/Documents/设计项目/廖哥雅居_室内设计总控/04_SU_Exports_View/R02_scene_exports"

set cmd to quoted form of py & " " & quoted form of bridge & " export-scenes " & quoted form of outDir & " 2400 1600 --timeout 240"
do shell script cmd
```

## 7. Avoid

Avoid all of these inside AppleScript:

```applescript
-- heredoc inside do shell script
do shell script "cat > /tmp/a.py <<'PY' ... PY"

-- inline python/ruby with quote nesting
do shell script "python3 -c \"print('bad')\""

-- unquoted Chinese or spaced paths
do shell script "python3 /Users/bonnie/Documents/设计项目/my script.py"
```

## 8. Prefer wrapper for repeat tasks

```applescript
set wrapper to "/Users/bonnie/Documents/设计项目/廖哥雅居_室内设计总控/run_r02_sketchup.command"
do shell script quoted form of wrapper
```
