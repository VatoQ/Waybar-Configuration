#!/bin/bash

#if pgrep -x "blueman-manager" >/dev/null; then
#  ##echo "Running"
#  pkill blueman-manager
#else
#  ##echo "Stopped"
#  blueman-manager
#fi

python /home/onath/.config/waybar/popup_manager/query_popup.py blueman-manager
