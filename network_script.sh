#!/bin/bash

#if pgrep -fx "nm-connection-editor" >/dev/null; then
#  pkill -f nm-connection-editor
#else
#  nm-connection-editor
#fi

python /home/onath/.config/waybar/popup_manager/query_popup.py network
