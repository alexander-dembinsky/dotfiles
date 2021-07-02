#!/bin/sh

LOCK_IMAGE=$(dirname "$0")/lock-image.png
ORIGINAL_WALLPAPER_FILE=$(awk -F '=' '/file/ {print $2}' ~/.config/nitrogen/bg-saved.cfg)

convert -blur 0x10 $ORIGINAL_WALLPAPER_FILE $LOCK_IMAGE

i3lock -i $LOCK_IMAGE

