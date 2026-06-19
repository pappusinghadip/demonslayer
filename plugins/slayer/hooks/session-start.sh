#!/usr/bin/env bash

set -euo pipefail

CORE_FILE="${CLAUDE_PLUGIN_ROOT}/skills/core-principles/SKILL.md"
PROJECT_CONTEXT="${CLAUDE_PROJECT_DIR}/.slayer/context/project.md"
MEMORY_INDEX="${CLAUDE_PROJECT_DIR}/.slayer/memory/long-term/index.md"

content=""

if [ -f "$CORE_FILE" ]; then
  content="$(cat "$CORE_FILE")"
fi

if [ -f "$PROJECT_CONTEXT" ]; then
  project_content="$(cat "$PROJECT_CONTEXT")"
  content="$content

## Slayers Project Context

$project_content"
fi

if [ -f "$MEMORY_INDEX" ]; then
  memory_content="$(cat "$MEMORY_INDEX")"
  content="$content

## Slayers Long-Term Memory

$memory_content"
fi

content="$content

## Slayers Skill-First Rule

Before starting Slayers workflow work, check whether an Slayers skill or slash command matches the request. Prefer the workflow over ad hoc execution when the task is multi-phase, repo-specific, git-sensitive, or production-adjacent."

printf '%s' "$content" | python3 -c '
import json
import sys

print(json.dumps({"additionalContext": sys.stdin.read()}))
'
