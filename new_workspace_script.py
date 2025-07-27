#!/bin/python
# Copyright (c) 2025 VatoQ
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

import subprocess
import json
import sys


def current_focus_workspace():
    monitor_list = (
        subprocess.run("hyprctl -j monitors".split(), stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .strip()
    )

    monitor_list = json.loads(monitor_list)
    for monitor in monitor_list:
        if monitor["focused"]:
            return [monitor["name"], monitor["activeWorkspace"]["id"]]
    return []


currentWorkspace = int(current_focus_workspace()[1])
currMonitor = current_focus_workspace()[0]

workspaceList = json.loads(
    subprocess.run("hyprctl -j workspaces".split(), stdout=subprocess.PIPE)
    .stdout.decode()
    .strip()
)

workSpacesOfMonitor = list(
    filter(lambda workspace: workspace["monitor"] == currMonitor, workspaceList)
)

workSpacesOfMonitor.sort(key=(lambda workspace: int(workspace["id"])), reverse=True)

highestWorkspaceOnMonitor = workSpacesOfMonitor[0]

if highestWorkspaceOnMonitor["id"] > currentWorkspace:
    if "--with-window" in sys.argv:
        subprocess.run("hyprctl dispatch movetoworkspace m+1".split())
    else:
        subprocess.run("hyprctl dispatch workspace m+1".split())

else:
    workspaceList.sort(key=(lambda workspace: workspace["id"]), reverse=True)

    highestWorkspaceId = workspaceList[0]["id"]

    if "--with-window" in sys.argv:
        subprocess.run(
            f"hyprctl dispatch movetoworkspace {highestWorkspaceId + 1}".split()
        )
    else:
        subprocess.run(f"hyprctl dispatch workspace {highestWorkspaceId + 1}".split())

    subprocess.run(
        f"hyprctl dispatch moveworkspacetomonitor {highestWorkspaceId + 1} {currMonitor}".split()
    )
