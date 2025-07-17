#!/bin/bash

#if pgrep -x "pavucontrol" >/dev/null; then
#  pkill pavucontrol
#else
#  pavucontrol
#fi

python /home/onath/.config/waybar/popup_manager/query_popup.py pavucontrol
