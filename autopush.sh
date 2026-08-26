#!/usr/bin/env bash
# Watch ONLY the 3 template files and auto commit+push on change. Run once, leave open.
# Usage: ./autopush.sh
cd "$(dirname "$0")" || exit 1
FILES="file1.py file2.py file3.py"
echo "auto-push watching: $FILES  (Ctrl-C to stop)"
while true; do
  if [ -n "$(git status --porcelain -- $FILES)" ]; then
    git add $FILES && git commit -q -m "auto $(date '+%Y-%m-%d %H:%M:%S')" && git push -q \
      && echo "pushed $(date '+%H:%M:%S')" || echo "push failed $(date '+%H:%M:%S')"
  fi
  sleep 5
done
