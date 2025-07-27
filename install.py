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


from install_resources import (
    generate_css,
    generate_json,
    generate_shell_scripts,
    generate_init,
)
import getpass
import subprocess
import argparse
from config import Config


# CALL ARGUMENT SECION -------------------------------------------------------------------------------------------------------
font_size_help = "specify the font size that the waybar elements are displayed at"
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "--font_size", nargs="?", help=font_size_help, const=30, type=int
)
args = arg_parser.parse_args()

font_size = args.font_size


# PATH INITIALIZATION ---------------------------------------------------------------------------------------------------------
states_found = False

current_user = getpass.getuser()
Config.set_target_path(current_user)

target_path_status = subprocess.call(["test", "-e", Config.TARGET_PATH])

if target_path_status != Config.EXISTS_STATUS:
    print(
        f"Waybar config directory not found, making new directory (status = {target_path_status})"
    )
else:
    print("Replacing contents of waybar config")

    json_status = subprocess.call(
        ["test", "-e", f"{Config.TARGET_PATH}/{Config.DAEMON_DIR}/pop_up_states.json"]
    )

    if json_status != Config.EXISTS_STATUS:
        print("caching existing pop up state cache")
        states_found = True
        subprocess.run(
            f"mv {Config.TARGET_PATH}/{Config.DAEMON_DIR}/pop_up_states.json cache".split()
        )

    shell_output = subprocess.run(
        f"rm -rf {Config.TARGET_PATH}".split(), stdout=subprocess.PIPE
    ).stdout.decode()


shell_output = subprocess.run(
    f"mkdir -p {Config.TARGET_PATH}".split(), stdout=subprocess.PIPE
).stdout.decode()

# CODE GENERATION AND INSTALLATION ---------------------------------------------------------------------------------------------------------------------------------------------

css_content = generate_css(current_user, font_size=font_size)

json_content = generate_json(current_user)

initializing_content = generate_init(current_user)

# Copy resource directories to .config/waybar
subprocess.run(f"cp -r icons {Config.TARGET_PATH}".split())
subprocess.run(f"cp -r popup_manager {Config.TARGET_PATH}".split())
# Copy scripts to .config/waybar
subprocess.run(f"cp new_workspace_script.py {Config.TARGET_PATH}".split())
subprocess.run(f"cp config.jsonc {Config.TARGET_PATH}".split())

shell_names = [
    "audio_script.sh",
    "bluetooth_script.sh",
    "calendar_script.sh",
    "network_script.sh",
    "new_workspace_script.sh",
]

shell_contents = generate_shell_scripts(current_user)

for s_name, s_content in zip(shell_names, shell_contents):
    with open(f"{Config.TARGET_PATH}/{s_name}", "w") as shell_file:
        shell_file.write(s_content)

    subprocess.run(f"chmod +x {Config.TARGET_PATH}/{s_name}".split())

with open(f"{Config.TARGET_PATH}/style.css", "w") as css_file:
    css_file.write(css_content)

with open(
    f"{Config.TARGET_PATH}/{Config.DAEMON_DIR}/initialize_states.py", "w"
) as init_file:
    init_file.write(initializing_content)

# POST INSTALLATION PROCESSES -----------------------------------------------------------------------------------------------------

subprocess.run("pkill waybar".split())
subprocess.Popen("waybar".split())

if states_found:
    print("restoring pop up state cache")
    subprocess.run(
        f"mv cache/pop_up_states.json {Config.TARGET_PATH}/{Config.DAEMON_DIR}/".split()
    )
