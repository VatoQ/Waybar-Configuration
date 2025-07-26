#!/bin/python

from install_resources import generate_css, generate_json, generate_shell_scripts
import getpass
import subprocess

TEST = False
EXISTS_STATUS = 0
DOES_NOT_EXIST_STATUS = 1


def get_target_path(test, current_user):
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
    shell_output = subprocess.run(
        f"rm -rf {TARGET_PATH}".split(), stdout=subprocess.PIPE
    ).stdout.decode()


shell_output = subprocess.run(
    f"mkdir -p {TARGET_PATH}".split(), stdout=subprocess.PIPE
).stdout.decode()


css_content = generate_css(current_user)

json_content = generate_json(current_user)


subprocess.run(f"cp -r icons {TARGET_PATH}".split())
subprocess.run(f"cp -r popup_manager {TARGET_PATH}".split())

# subprocess.run(f"cp audio_script.sh {TARGET_PATH}".split())
# subprocess.run(f"cp bluetooth_script.sh {TARGET_PATH}".split())
# subprocess.run(f"cp calendar_script.sh {TARGET_PATH}".split())
# subprocess.run(f"cp network_script.sh {TARGET_PATH}".split())
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

# with open(f"{TARGET_PATH}/config.jsonc", "w") as json_file:
#    json_file.write(json_content)


subprocess.run("pkill waybar".split())
subprocess.Popen("waybar".split())
