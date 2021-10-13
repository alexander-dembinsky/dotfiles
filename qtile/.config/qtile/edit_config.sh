#!/usr/bin/env bash

config_name=`ls -la ~/.config | tail -n +4 | awk '{print $9}' | rofi -p "Edit Config" -dmenu`
selected_config=$HOME/.config/$config_name

alacritty -e nvim $selected_config

