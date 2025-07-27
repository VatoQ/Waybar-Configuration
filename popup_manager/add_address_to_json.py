#!/bin/python

import argparse
import json
import subprocess
from pprint import pprint

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

window_name = window_names[pop_up_index]
with open("pop_up_states.json") as json_file:
    json_data = json.load(json_file)
window_state = json_data[pop_up_index]


def get_window_address(argument: str, message: list[dict]):
    """
    Look up window address in the cache, based on the argument passed on call.

    :param argument: valid arguments are the following:
    :param message: List of hyprctl cliens
    """
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


windows = json.loads(
    subprocess.run("hyprctl -j clients".split(), stdout=subprocess.PIPE)
    .stdout.decode()
    .strip()
)

address = get_window_address(window_name, windows)

window_state["address"] = address

with open("pop_up_states.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)
