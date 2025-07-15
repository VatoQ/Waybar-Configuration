#!/bin/python

import argparse
import json

pop_up_name_help = (
    "Choose, which window to query:"
    "\n\t0: wlogout,"
    "\n\t1: blueman-manager,"
    "\n\t2: network,"
    "\n\t3: pavucontrol,"
    "\n\t4: calendar"
)

parser = argparse.ArgumentParser()
parser.add_argument("pop_up_index", help=pop_up_name_help, type=int)

args = parser.parse_args()


pop_up_index = args.pop_up_index


window_names = ["wlogout", "blueman-manager", "network", "pavucontrol", "calendar"]


window_name = window_names[pop_up_index]

with open("pop_up_states.jsonr") as json_file:
    json_data = json.load(json_file)

window_state = json_data[window_name]


# TODO:
