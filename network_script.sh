#!/bin/bash

if pgrep -fx "nm-connection-editor" >/dev/null; then
  pkill -f nm-connection-editor
else
  nm-connection-editor
fi
