# Imagegen Routing Misstatement Blocking Warning

Date: 2026-07-10

## Incident

Codex previously made an incorrect statement about Bonnie's image-generation routing behavior by describing built-in `image_gen` as the default-priority route in an environment that had already been redirected to the WE-AI AZ CLI/API route.

## Impact classification

- Severity: blocking
- Risk type: routing misstatement / false operational status claim
- Business impact: user states this class of error can contribute to major commercial loss

## Mandatory rule going forward

For any future claim about Bonnie image-generation behavior, availability, default routing, active endpoint, or route migration state:

1. Check effective local configuration first.
2. Verify the active route with at least one real API/CLI call or an equivalent executable validation.
3. Do not describe built-in `image_gen` as active/default unless that route has been explicitly reconfigured and re-verified.
4. Do not describe routing status from memory, prior defaults, generic Codex behavior, or unverified assumptions.

## Concrete protected assertions

The following statements require verification before they are presented as fact:

- whether image generation currently works
- whether Bonnie's environment uses built-in `image_gen`
- whether Bonnie's environment uses the WE-AI AZ CLI/API route
- whether the active generation endpoint is `/v1/images/generations`
- whether the active edit endpoint is `/v1/images/edits`
- whether Responses API is or is not involved

## Current enforced policy

- Bonnie image generation is CLI/API-only.
- The route must use the WE-AI AZ configuration.
- Generation must use `/v1/images/generations`.
- Editing must use `/v1/images/edits`.
- Responses API must not be used for image generation.

