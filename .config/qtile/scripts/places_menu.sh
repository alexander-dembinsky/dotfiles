#!/usr/bin/env bash

FILEMAN="thunar"

(cat <<EOF
Home,$FILEMAN $HOME
Downloads,$FILEMAN $HOME/Downloads
Pictures,$FILEMAN $HOME/Pictures
SSD,$FILEMAN /mnt/SSD
HDD,$FILEMAN /mnt/HDD
EOF
) | jgmenu --simple --at-pointer --config-file=$HOME/.config/qtile/scripts/jgmenurc
