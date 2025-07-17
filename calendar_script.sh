#!/bin/bash

#if pgrep -x "gnome-calendar" >/dev/null; then
#  pkill gnome-calendar
#else
#  gnome-calendar
#fi

python /home/onath/.config/waybar/popup_manager/query_popup.py calendar
