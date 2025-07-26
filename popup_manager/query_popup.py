#!/bin/python

import argparse
import json
import shlex
import subprocess
import getpass
from pprint import pprint

USER = getpass.getuser()

current_location = f"/home/{USER}/.config/waybar/popup_manager/"


def get_window_address(argument: str, message: list[dict]):
    if __debug__:
        print(f"\t\tEntering get_window_address({argument})")
    for item in message:
        if __debug__:
            print(f"\t\tsearching class:{item['class']}")
        if argument in item["class"]:
            if __debug__:
                print("\t\tFound a matching window:")
                pprint(item)
            return item["address"]
    return "None"


TIMER_MINUTES = 30


pop_up_name_help = (
    "Choose, which window to query: "
    "\n\tblueman-manager, "
    "\n\tnetwork, "
    "\n\tpavucontrol, "
    "\n\tcalendar"
)

parser = argparse.ArgumentParser()
parser.add_argument("pop_up_index", help=pop_up_name_help, type=str)
args = parser.parse_args()
pop_up_index = args.pop_up_index


window_names = {
    "blueman-manager": "blueman-manager",
    "network": "nm-connection-editor",
    "pavucontrol": "org.pulseaudio.pavucontrol",
    "calendar": "org.gnome.Calendar",
}

bash_processes = {
    "blueman-manager": "blueman-manager",
    "network": "nm-connection-editor",
    "pavucontrol": "pavucontrol",
    "calendar": "gnome-calendar",
}


if pop_up_index not in window_names.keys():
    raise ValueError(f"No window {pop_up_index} found in manager")

window_name = window_names[pop_up_index]
bash_process_name = bash_processes[pop_up_index]
with open(current_location + "pop_up_states.json") as json_file:
    json_data = json.load(json_file)

window_state = json_data[pop_up_index]

if __debug__:
    print("Entering debug session.")
    print(f"\tPassed Argument: {pop_up_index}")
    print(f"\tWindow name: {window_name}")
    print(f"\tBash name: {bash_process_name}")
    print("Window state:")
    pprint(window_state)

if window_state["active"] and window_state["focused"]:
    if __debug__:
        print("Case: Window is active and focused")

    move_to_special_command_raw = (
        f"hyprctl dispatch movetoworkspacesilent special,class:^({window_name})$"
    )
    move_args = move_to_special_command_raw.split()
    if __debug__:
        print(f"\tcommand: {move_to_special_command_raw}")
        print(f"\tcommand list: {move_args}")
    subprocess.run(move_args)

    window_state["focused"] = False

elif window_state["active"] and not window_state["focused"]:
    if __debug__:
        print("Case: Window active but minimized")
    active_ws_command_raw = "hyprctl -j activeworkspace"
    active_args = shlex.split(active_ws_command_raw)

    if __debug__:
        print(f"\tcommand: {active_ws_command_raw}")
        print(f"\tcommand list: {active_args}")
    open_windows = json.loads(
        subprocess.run("hyprctl -j clients".split(), stdout=subprocess.PIPE)
        .stdout.decode()
        .strip()
    )

    current_workspace_id = json.loads(
        subprocess.run("hyprctl -j activeworkspace".split(), stdout=subprocess.PIPE)
        .stdout.decode()
        .strip()
    )["id"]
    if __debug__:
        print(f"\tworkspace id: {current_workspace_id}")

    window_address = get_window_address(window_name, open_windows)

    if window_address == "None":
        if __debug__:
            print("\tNo window found. Trying to find it by address")

        subprocess.run(f"hyprctl dispatch exec {bash_process_name}".split())

        window_address = window_state.get("address", None)
        if not window_address:
            open_windows = json.loads(
                subprocess.run("hyprctl -j clients".split(), stdout=subprocess.PIPE)
                .stdout.decode()
                .strip()
            )

        else:
            print("\t\taddress found")
            subprocess.run(
                f"hyprctl dispatch movetoworkspacesilent {current_workspace_id}, class:^({window_name})$".split()
            )

    else:
        print(f"\tMoving window to workspace {current_workspace_id}")
        subprocess.run(
            f"hyprctl dispatch movetoworkspacesilent {current_workspace_id}, class:^({window_name})$".split()
        )
    if __debug__:
        print(f"\tworkspacewindow address:{window_address}")

    window_state["focused"] = True
else:
    if __debug__:
        print("Case: No window active")
    window_state["active"] = True
    subprocess.run(f"hyprctl dispatch exec {bash_process_name}".split())


json_data[pop_up_index] = window_state

with open(current_location + "pop_up_states.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)
