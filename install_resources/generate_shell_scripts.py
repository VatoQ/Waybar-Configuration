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


def generate_shell_scripts(current_user):
    """
    Generates the shell scripts that are called by waybar.

    :param current_user str: current user to ensure correct script paths in the shell scripts.
    """
    path = f"/home/{current_user}/.config/waybar/popup_manager/query_popup.py"

    audio = "pavucontrol"

    bluetooth = "blueman-manager"

    calendar = "calendar"

    network = "network"

    return (
        f"{path} {audio}",
        f"{path} {bluetooth}",
        f"{path} {calendar}",
        f"{path} {network}",
    )
