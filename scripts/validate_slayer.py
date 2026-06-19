#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "slayer"

AGENTS = {
    "kagaya",
    "tanjiro",
    "mitsuri",
    "tamayo",
    "doma",
    "obanai",
    "akaza",
    "zenitsu",
    "gyomei",
    "tengen",
    "yushiro",
}

COMMANDS = {
    "audit",
    "brainstorm",
    "plan",
    "feature",
    "bugfix",
    "fix",
    "debug",
    "explain",
    "pr",
    "refactor",
    "report",
    "research",
    "review",
    "test",
    "commit",
    "init",
    "documentation",
}
SKILLS = {
    "audit-first",
    "auto-init",
    "build-patterns",
    "kagaya",
    "core-principles",
    "git-safety",
    "akaza",
    "memory",
    "tengen",
    "scoped-fix",
    "test-strategies",
    "verification",
    "php",
    "android",
    "kmm",
    "design-routing",
    "minimal-code",
}
KNOWLEDGE = {
    "build-patterns.md",
    "core-principles.md",
    "workflow-rules.md",
    "review-checklist.md",
    "security-checklist.md",
    "testing-checklist.md",
    "test-strategies.md",
    "git-rules.md",
    "memory-system.md",
    "php.md",
    "android.md",
    "kmm.md",
    "design-routing.md",
    "minimal-code.md",
}
SAFETY_PHRASES = {
    PLUGIN / "knowledge" / "core-principles.md": [
        "## Rule Precedence",
        "## Remote Write Safety",
        "## Read-Only Shell Safety",
        "## Secrets And Sensitive Data",
    ],
    PLUGIN / "knowledge" / "workflow-rules.md": [
        "Follow `Remote Write Safety` in `core-principles.md`",
        "## Gate Handling",
        "Do not write secrets",
    ],
    PLUGIN / "knowledge" / "build-patterns.md": [
        "Parallel dispatch is allowed only for non-overlapping file sets",
        "If two agents may touch the same file",
    ],
    PLUGIN / "knowledge" / "git-rules.md": [
        "Remote writes follow `Remote Write Safety` in `core-principles.md`",
    ],
    PLUGIN / "agents" / "obanai.md": ["Bash is for inspection only"],
    PLUGIN / "agents" / "doma.md": [
        "Bash is for inspection only",
        "Never print or write secret values",
    ],
    PLUGIN / "agents" / "akaza.md": ["Bash is for inspection and verification only"],
    PLUGIN / "agents" / "tengen.md": [
        "Bash is inspection-only until an explicit approved git action",
        "Remote writes follow `Remote Write Safety`",
    ],
    PLUGIN / "agents" / "kagaya.md": [
        "Dispatch parallel editors only for non-overlapping file sets",
        "consult `design-routing`",
    ],
    PLUGIN / "agents" / "mitsuri.md": [
        "If invoked directly, own only the files needed",
        "consult `design-routing`",
    ],
    PLUGIN / "agents" / "tamayo.md": ["If invoked directly, own only the files needed"],
    PLUGIN / "agents" / "zenitsu.md": ["If invoked directly, own only the files needed"],
    PLUGIN / "agents" / "gyomei.md": ["If invoked directly, own only the files needed"],
    PLUGIN / "agents" / "yushiro.md": ["Never write secrets"],
    PLUGIN / "commands" / "feature.md": ["## Gate Handling", "Do not write secrets"],
    PLUGIN / "commands" / "bugfix.md": ["## Gate Handling", "Do not write secrets"],
    PLUGIN / "commands" / "commit.md": ["Remote writes follow `Remote Write Safety`"],
    PLUGIN / "commands" / "pr.md": ["Remote writes follow `Remote Write Safety`"],
    PLUGIN / "commands" / "documentation.md": [
        "Do not edit source code",
        "self-contained",
    ],
    PLUGIN / "knowledge" / "php.md": [
        "Apply only when the project uses PHP",
        "## Clean Architecture",
        "Dependencies point inward",
    ],
    PLUGIN / "knowledge" / "android.md": [
        "Apply only when the project targets Android",
        "## Clean Architecture",
        "Unidirectional data flow",
    ],
    PLUGIN / "knowledge" / "kmm.md": [
        "Apply only when the project has a shared Kotlin Multiplatform module",
        "## Clean Architecture",
        "Dependency inversion across the platform boundary",
    ],
    PLUGIN / "knowledge" / "design-routing.md": [
        "## Routing Matrix",
        "Hand-Build Principles",
    ],
    PLUGIN / "knowledge" / "minimal-code.md": [
        "## The Reuse Ladder",
        "The Floor — never cut these",
    ],
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        fail(f"{path} is not valid JSON: {exc}")


def frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(f"{path} is missing YAML frontmatter")
    data: dict[str, object] = {}
    current: str | None = None
    for raw in match.group(1).splitlines():
        if re.match(r"^[A-Za-z0-9_-]+:", raw):
            key, value = raw.split(":", 1)
            current = key.strip()
            data[current] = value.strip()
        elif raw.startswith("  - ") and current:
            data.setdefault(current, [])
            if not isinstance(data[current], list):
                data[current] = []
            data[current].append(raw[4:].strip())
    return data


def main() -> None:
    read_json(ROOT / ".codex-plugin" / "plugin.json")
    marketplace = read_json(ROOT / ".claude-plugin" / "marketplace.json")
    plugin_json = read_json(PLUGIN / ".claude-plugin" / "plugin.json")

    if marketplace["plugins"][0]["version"] != plugin_json["version"]:
        fail("Claude marketplace and plugin versions differ")

    for agent in AGENTS:
        path = PLUGIN / "agents" / f"{agent}.md"
        if not path.exists():
            fail(f"missing agent {agent}")
        fm = frontmatter(path)
        if fm.get("name") != agent:
            fail(f"agent name mismatch in {path}")
        for skill in fm.get("skills", []):
            if skill not in SKILLS:
                fail(f"{path} references missing skill {skill}")

    for command in COMMANDS:
        path = PLUGIN / "commands" / f"{command}.md"
        if not path.exists():
            fail(f"missing command {command}")
        fm = frontmatter(path)
        if "description" not in fm or "allowed-tools" not in fm:
            fail(f"command metadata incomplete in {path}")

    for skill in SKILLS:
        path = PLUGIN / "skills" / skill / "SKILL.md"
        if not path.exists():
            fail(f"missing skill {skill}")
        fm = frontmatter(path)
        if fm.get("name") != skill:
            fail(f"skill name mismatch in {path}")

    for knowledge in KNOWLEDGE:
        if not (PLUGIN / "knowledge" / knowledge).exists():
            fail(f"missing knowledge file {knowledge}")

    hooks = PLUGIN / "hooks" / "hooks.json"
    session_start = PLUGIN / "hooks" / "session-start.sh"
    if not hooks.exists():
        fail("missing hooks/hooks.json")
    read_json(hooks)
    if not session_start.exists():
        fail("missing hooks/session-start.sh")
    if not (session_start.stat().st_mode & 0o111):
        fail("hooks/session-start.sh is not executable")

    for path, phrases in SAFETY_PHRASES.items():
        text = path.read_text()
        for phrase in phrases:
            if phrase not in text:
                fail(f"missing safety phrase {phrase!r} in {path}")

    forbidden_parts = [
        ("Shankar", "Kakumani"),
        ("shankar", "@"),
        ("transformers", "@", "transformers"),
        (".claude", "transformers"),
    ]
    for path in ROOT.rglob("*"):
        if path == Path(__file__).resolve():
            continue
        if path.is_file() and ".git" not in path.parts:
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                continue
            for parts in forbidden_parts:
                token = "".join(parts)
                if token in text:
                    fail(f"forbidden upstream token {token!r} in {path}")

    print("OK: Slayer Agents structure is valid")


if __name__ == "__main__":
    main()
