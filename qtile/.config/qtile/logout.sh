#!/usr/bin/env bash

SUSPEND="Suspend"
LOGOUT="Logout"
REBOOT="Reboot"
POWEROFF="Poweroff"

choise=`rofi -dmenu -i -p "Exit" -matching fuzzy << EOM
${SUSPEND}
${LOGOUT}
${REBOOT}
${POWEROFF}
EOM`

case $choise in 
	"${SUSPEND}") 
		systemctl suspend;;
	"${LOGOUT}")
		qtile cmd-obj -o cmd -f shutdown;;
	"${REBOOT}")
		systemctl reboot;;
	"${POWEROFF}")
		systemctl poweroff;;
esac
