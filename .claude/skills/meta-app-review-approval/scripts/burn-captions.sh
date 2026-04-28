#!/usr/bin/env bash
# Burn Netflix-style yellow captions onto a screen-recorded MP4.
#
# Why .ass instead of .srt:
#   - .ass lets us set PlayResY=2160 explicitly. Without that, libass
#     defaults to PlayResY=288 and scales FontSize by ~7.5x on a 4K
#     video, making captions absurdly large.
#   - .ass also gives us BorderStyle=1 (outline only, not opaque box),
#     which is the Netflix look.
#
# Style: yellow text (&H0000FFFF in ASS BGR), black 3px outline,
# bottom-center, MarginV=120 from bottom.
#
# Usage:
#   ./burn-captions.sh <input.mp4> <captions.ass> <output.mp4>
#
# Example:
#   ./burn-captions.sh ~/Downloads/meta.mp4 \
#     ~/.claude/skills/meta-app-review-approval/assets/captions-template.ass \
#     ~/Downloads/meta-captioned.mp4

set -euo pipefail

INPUT="${1:?usage: burn-captions.sh <input.mp4> <captions.ass> <output.mp4>}"
CAPTIONS="${2:?missing captions file}"
OUTPUT="${3:?missing output path}"

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ERROR: ffmpeg not installed. brew install ffmpeg" >&2
  exit 1
fi

ffmpeg -y -i "$INPUT" \
  -vf "ass=$CAPTIONS" \
  -c:a copy \
  -preset fast \
  "$OUTPUT"

echo "Done. Output: $OUTPUT"
echo "Tip: extract a frame to verify caption styling:"
echo "  ffmpeg -ss 2 -i $OUTPUT -frames:v 1 -q:v 2 /tmp/preview.jpg -y"
