#!/usr/bin/env bash

config_name=`ls -la ~/.config | tail -n +4 | awk '{print $9}' | rofi -p "Edit Config" -dmenu`
selected_config=$HOME/.config/$config_name

if [[ -d "$selected_config" ]];
then
	cd $selected_config && alacritty -e nvim
else
	alacritty -e nvim $selected_config
fi

