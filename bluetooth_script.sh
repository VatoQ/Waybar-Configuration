#!/bin/bash

if pgrep -x "blueman-manager" >/dev/null; then
  ##echo "Running"
  pkill blueman-manager
else
  ##echo "Stopped"
  blueman-manager
fi
