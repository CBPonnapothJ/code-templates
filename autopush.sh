#!/usr/bin/env bash
# Watch this repo and auto commit+push on every change. Run once, leave open.
# Usage: ./autopush.sh
cd "$(dirname "$0")" || exit 1
echo "auto-push watching $(pwd)  (Ctrl-C to stop)"
while true; do
  if [ -n "$(git status --porcelain)" ]; then
    git add -A && git commit -q -m "auto $(date '+%Y-%m-%d %H:%M:%S')" && git push -q \
      && echo "pushed $(date '+%H:%M:%S')" || echo "push failed $(date '+%H:%M:%S')"
  fi
  sleep 5
done
