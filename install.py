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


from install_resources import generate_css, generate_json, generate_shell_scripts
import getpass
import subprocess
import argparse

TEST = False
EXISTS_STATUS = 0
DOES_NOT_EXIST_STATUS = 1


states_found = False

font_size_help = "specify the font size that the waybar elements are displayed at"

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "--font_size", nargs="?", help=font_size_help, const=30, type=int
)
args = arg_parser.parse_args()

font_size = args.font_size


def get_target_path(test, current_user):
    """
    Returns the target path of the installation

    Depending on which mode the script runs on, it is either the `.config` directory or in Documents

    Parameters
    ----------
    test : bool

        sets the mode of the script
    current_user : str
        current user to ensure a working installation.
    """
    if test:
        return f"/home/{current_user}/Documents/Private/Coding/Python/TestWaybarInstall"

    else:
        return f"/home/{current_user}/.config/waybar"


current_user = getpass.getuser()

TARGET_PATH = get_target_path(TEST, current_user)

target_path_status = subprocess.call(["test", "-e", TARGET_PATH])

if target_path_status != EXISTS_STATUS:
    print(
        f"Waybar config directory not found, making new directory (status = {target_path_status})"
    )
else:
    print("Replacing contents of waybar config")

    json_status = subprocess.call(
        ["test", "-e", f"{TARGET_PATH}/popup_manager/pop_up_states.json"]
    )

    if json_status != EXISTS_STATUS:
        print("caching existing pop up state cache")
        states_found = True
        subprocess.run(
            f"mv {TARGET_PATH}/popup_manager/pop_up_states.json cache".split()
        )

    shell_output = subprocess.run(
        f"rm -rf {TARGET_PATH}".split(), stdout=subprocess.PIPE
    ).stdout.decode()


shell_output = subprocess.run(
    f"mkdir -p {TARGET_PATH}".split(), stdout=subprocess.PIPE
).stdout.decode()


css_content = generate_css(current_user, font_size=font_size)

json_content = generate_json(current_user)

# Copy resource directories to .config/waybar
subprocess.run(f"cp -r icons {TARGET_PATH}".split())
subprocess.run(f"cp -r popup_manager {TARGET_PATH}".split())
# Copy scripts to .config/waybar
subprocess.run(f"cp new_workspace_script.py {TARGET_PATH}".split())
subprocess.run(f"cp config.jsonc {TARGET_PATH}".split())

shell_names = [
    "audio_script.sh",
    "bluetooth_script.sh",
    "calendar_script.sh",
    "network_script.sh",
    "new_workspace_script.sh",
]

shell_contents = generate_shell_scripts(current_user)

for s_name, s_content in zip(shell_names, shell_contents):
    with open(f"{TARGET_PATH}/{s_name}", "w") as shell_file:
        shell_file.write(s_content)

    subprocess.run(f"chmod +x {TARGET_PATH}/{s_name}".split())

with open(f"{TARGET_PATH}/style.css", "w") as css_file:
    css_file.write(css_content)


subprocess.run("pkill waybar".split())
subprocess.Popen("waybar".split())

if states_found:
    print("restoring pop up state cache")
    subprocess.run(f"mv cache/pop_up_states.json {TARGET_PATH}/popup_manager/".split())
