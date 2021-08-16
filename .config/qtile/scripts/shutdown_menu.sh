#!/usr/bin/env bash

(cat <<EOF
Logout,      qtile cmd-obj -o cmd -f shutdown, system-log-out
Suspend,     systemctl -i suspend            , system-suspend
Reboot,      systemctl -i reboot             , system-reboot
^sep()
Power Off,   systemctl -i poweroff           , system-shutdown
EOF
) | jgmenu --simple --at-pointer --config-file=$HOME/.config/qtile/scripts/jgmenurc
