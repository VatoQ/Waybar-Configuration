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
