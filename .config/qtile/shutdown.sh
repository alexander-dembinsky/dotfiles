#!/usr/bin/env bash

LOGOUT=" Log Out"
SUSPEND=" Suspend"
REBOOT=" Reboot"
POWEROFF=" Power Off"

session=`loginctl session-status | head -n 1 | awk '{print $1}'`
printf "$LOGOUT,loginctl terminate-session ${session}\n$SUSPEND,systemctl suspend\n$REBOOT,systemctl reboot\n$POWEROFF,systemctl poweroff\n" | jgmenu --simple --at-pointer

