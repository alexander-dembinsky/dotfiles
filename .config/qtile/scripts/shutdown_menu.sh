#!/usr/bin/env bash

(cat <<EOF
Logout,      qtile cmd-obj -o cmd -f shutdown
Suspend,     systemctl suspend
Reboot,      systemctl reboot
^sep()
Power Off,   systemctl poweroff
EOF
) | jgmenu --simple --at-pointer --config-file=$HOME/.config/qtile/scripts/jgmenurc
