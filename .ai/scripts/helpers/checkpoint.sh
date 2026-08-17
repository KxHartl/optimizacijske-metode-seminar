#!/usr/bin/env bash
# One-shot checkpoint commit (LiteRealm rule 1: proactive git).
# Usage:
#   Autonomous AI commit: ./.ai/scripts/helpers/checkpoint.sh "feat(scope): description"
#   User-driven commit:   ./.ai/scripts/helpers/checkpoint.sh --user "feat(scope): description"
set -euo pipefail

user_driven=false
if [ "${1:-}" = "--user" ] || [ "${1:-}" = "-u" ] || [ "${1:-}" = "--no-ai" ]; then
    user_driven=true
    shift
fi

msg="${1:?Usage: checkpoint.sh [--user] \"type: message\"}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
ai="🤖 [AI]"

if [ -z "$(git -C "$root" status --porcelain)" ]; then
    echo "Nothing to commit - working tree clean."
    exit 0
fi

if [ "$user_driven" = true ]; then
    if [[ ! "$msg" =~ ^[a-z]+(\([^\)]+\))?\!?:\ *(.+)$ ]]; then
        msg="chore: ${msg}"
    fi
else
    if [[ "$msg" != *"[AI]"* ]]; then
        if [[ "$msg" =~ ^[a-z]+(\([^\)]+\))?\!?:\ *(.+)$ ]]; then
            # Conventional commit: insert the marker after "type(scope):".
            prefix="${msg%%:*}"
            rest="${msg#*:}"
            msg="${prefix}: ${ai}${rest:+ }$(echo "$rest" | sed 's/^ *//')"
        else
            msg="chore: ${ai} ${msg}"
        fi
    fi
fi

git -C "$root" add -A
git -C "$root" commit -m "$msg"
