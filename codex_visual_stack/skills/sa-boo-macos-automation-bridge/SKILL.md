---
name: sa-boo-macos-automation-bridge
description: SA&BOO macOS automation bridge standard. Use when Codex needs to automate macOS apps, Finder, SketchUp, Terminal, AppleScript, JXA, shell scripts, Python/Ruby/Node scripts, or build reliable Mac workflow glue. Hard rule: AppleScript is only a thin orchestration shell; complex logic must live in external testable scripts. Must produce AppleScript-safe commands, quote paths with quoted form of, avoid heredoc/inlined code inside do shell script, and separate Terminal-safe, AppleScript-safe, JXA-safe, and app-native script layers.
---

# SA&BOO macOS Automation Bridge

This skill defines the long-term SA&BOO standard for Mac automation.

## Prime doctrine

**AppleScript is the shell, not the brain.**

Use AppleScript for:

- activating apps,
- opening files,
- light UI scripting,
- calling stable external scripts,
- connecting automation layers.

Do **not** put complex business/design/modeling logic inside AppleScript strings.

Complex logic must live in external, versioned, testable files:

- `.py` for filesystem/API/socket/data/image work,
- `.rb` for SketchUp Ruby / app-native Ruby logic,
- `.sh` for short shell wrappers only,
- `.js` / JXA for macOS automation when AppleScript is too brittle,
- MCP tools when available.

Target architecture:

```text
AppleScript outer shell
→ quoted call to external script
→ Python/Ruby/Node/Shell does real work
→ outputs JSON/text/image/model files
→ AppleScript optionally opens/reveals result
```

## Non-negotiable rules

1. **No heredoc inside `do shell script`.**
   - Bad: `do shell script "cat > file <<'PY' ... PY"`
   - Good: create the `.py` file separately, then call it.

2. **No large inline code inside AppleScript strings.**
   - Bad: `python3 -c "huge code with quotes"`
   - Good: `python3 /path/to/script.py args...`

3. **Always use `quoted form of` for paths and user strings.**

4. **Do not rely on shell profile state.**
   `do shell script` does not load the same environment as interactive Terminal.
   Use absolute paths for runtimes and scripts.

5. **Separate command safety levels.**
   Label snippets as:
   - Terminal-safe,
   - AppleScript-safe,
   - JXA-safe,
   - SketchUp Ruby-safe,
   - MCP-safe.

6. **Return machine-readable output when possible.**
   External scripts should print JSON for status, paths, errors, and next steps.

7. **Prefer idempotent scripts.**
   Re-running should not corrupt the project. Use versioned filenames and safe overwrite rules.

8. **Fail visibly.**
   On error, return a concise message and log path. Do not silently ignore automation failures.

9. **Never modify AiMaMi/local proxy configuration unless explicitly instructed.**
   SA&BOO automation may add project scripts and skills, but must not tamper with relay/proxy internals.

## AppleScript-safe command template

```applescript
set py to "/absolute/path/to/python3"
set scriptPath to "/absolute/path/to/script.py"
set arg1 to "/absolute/path/with spaces/中文路径/file.dxf"

set cmd to quoted form of py & " " & quoted form of scriptPath & " " & quoted form of arg1
do shell script cmd
```

With output capture:

```applescript
set resultText to do shell script cmd
return resultText
```

Reveal output:

```applescript
set outputFile to "/absolute/path/to/output.png"
tell application "Finder"
  reveal POSIX file outputFile
  activate
end tell
```

## Shell wrapper rule

If AppleScript needs to trigger a long chain, create a short `.command` or `.sh` wrapper:

```bash
#!/usr/bin/env bash
set -euo pipefail
PY="/absolute/python3"
ROOT="/absolute/project/root"
"$PY" "$ROOT/scripts/task.py" "$@"
```

Then AppleScript calls only the wrapper:

```applescript
set wrapper to "/absolute/project/run_task.command"
do shell script quoted form of wrapper
```

## SketchUp rule

Do not push large Ruby through AppleScript.

Preferred route:

```text
AppleScript
→ python sketchup_socket_bridge.py load /path/to/task.rb
→ SketchUp Ruby executes from file
→ python sketchup_socket_bridge.py export-scenes /path/out
```

Do not do:

```text
AppleScript → paste huge Ruby into SketchUp Ruby Console
```

## Browser / UI scripting rule

Use AppleScript UI scripting only when no API/MCP/CLI exists. UI scripting must be small and robust:

- activate app,
- wait for process/window,
- click/menu by stable labels,
- no long logic,
- add timeouts and clear failure notes.

## Output pattern

When this skill is used, respond with:

```text
自动化目标：
推荐层级：AppleScript / external script / MCP / app-native
AppleScript-safe 调用：
外置脚本路径：
测试命令：
风险点：
下一步：
```

## Long-term SA&BOO standard

Every repeated Mac workflow should eventually become:

```text
1. project script
2. AppleScript-safe launcher
3. log/output convention
4. visual or file checkpoint
5. QA note
6. skill documentation
```

The goal is stable creative automation: beautiful outputs, reliable execution, no quote hell.
