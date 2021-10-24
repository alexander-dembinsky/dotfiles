#!/usr/bin/env bash

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

# Disable TV by default
test -e ~/.bin/tv && ~/.bin/tv off

run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 
run nm-applet 
run blueberry-tray 
run nitrogen --restore 
run pamac-tray 
run picom --conf ~/.config/qtile/picom.conf
#run cbatticon -i notification 
