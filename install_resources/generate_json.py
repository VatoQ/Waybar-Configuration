def generate_json(current_user: str) -> str:
    """
    Generates the json file to config waybar.

    This is not currently used, but may find application in future versions.

    Parameters
    ----------
    current_user
        current user to ensure working installation.

    Returns
    -------
    str
        json file as a string.
    """
    with open("install_resources/json_content.txt", "r") as json_file:
        lines = json_file.readlines()

    return "".join(lines)
