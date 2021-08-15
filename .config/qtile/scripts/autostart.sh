#!/bin/bash

function run {
	if ! pgrep $1 ;
	then
		$@&
	fi
}

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
run sxhkd -c ~/.config/qtile/scripts/sxhkdrc &
run picom --config ~/.config/qtile/scripts/picom.conf &
run nm-applet &
run pamac-tray &
run volumeicon &
run blueman-applet &
run dunst -conf ~/.config/qtile/scripts/dunstrc &
run nitrogen --restore &
run variety &
run conky -c ~/.config/qtile/scripts/conky.conf &
