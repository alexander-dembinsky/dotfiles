#!/usr/bin/env bash

LOGOUT=" Log Out"
SUSPEND=" Suspend"
REBOOT=" Reboot"
POWEROFF=" Power Off"

ACTION=`echo -e "$LOGOUT\n Suspend\n Reboot\n Power Off" | rofi -dmenu -p Shutdown -l 4`

case "$ACTION" in
	"$LOGOUT")
		session=`loginctl session-status | head -n 1 | awk '{print $1}'`
		loginctl terminate-session $session
		;;
	"$SUSPEND") 
		systemctl suspend
		;;
	"$REBOOT")
		systemctl reboot
		;;
	"$POWEROFF")
		systemctl poweroff
		;;
esac
