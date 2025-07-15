#!/bin/python
"""
Initialize states of the pop up windows.
"""

import json

TIMER_MINUTES = 30

window_names = ["wlogout", "blueman-manager", "network", "pavucontrol", "calendar"]


pop_up_states = {}

for name in window_names:
    pop_up_states[name] = {
        "active": False,
        "focused": False,
        "timer": 0,
    }

with open("pop_up_states.json", "w") as json_file:
    json.dump(pop_up_states, json_file, indent=4)
