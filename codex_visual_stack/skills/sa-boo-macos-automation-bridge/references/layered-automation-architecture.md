# Layered Automation Architecture

## SA&BOO recommended stack

```text
User intent
→ Codex / skill routing
→ AppleScript-safe launcher when Mac UI needed
→ external script or MCP
→ app-native script if needed
→ file/image/model checkpoint
→ QA and iteration
```

## Layer responsibilities

### AppleScript

- App activation.
- Finder reveal/open.
- Small UI interaction.
- Calls external scripts with quoted paths.

### Python

- File operations.
- JSON status.
- Image/PDF processing.
- Socket bridges.
- API calls.
- Batch orchestration.

### Ruby / SketchUp Ruby

- SketchUp model creation.
- Scenes/cameras/materials/tags.
- Import/export inside SketchUp.

### Shell

- Tiny wrappers only.
- Never hold complex logic when Python/Ruby is better.

### MCP

- Preferred direct tool interface when available.
- Should expose semantic tools, not just raw eval.

## Good SketchUp loop

```text
Python socket bridge
→ load project Ruby file
→ model saved
→ scenes exported
→ Codex views PNG
→ Ruby revised
→ repeat
```

## Bad SketchUp loop

```text
AppleScript paste code into Ruby Console
→ modal popup
→ manual export
→ unclear state
```
