def generic_icon_style(current_user, selector, icon_name, **kwargs):
    out = [f"#{selector}", "\n", "{\n"]

    if kwargs.get("hover", None) and kwargs.get("hover") is True:
        out[0] += ":hover"
        icon_name += "-hover"
    else:
        icon_name += "-inactive"

    image_url = f"/home/{current_user}/.config/waybar/icons/{icon_name}.svg"

    image_style = f"    background-image: url('{image_url}');\n"

    # out.append(image_style)

    out += [image_style]

    if kwargs.get("margin", None):
        margin_type = kwargs.get("margin")

        margin_style = "    margin"

        if margin_type in ["left", "l"]:
            margin_style += "-left"

        elif margin_type in ["right", "r"]:
            margin_style += "-right"

        elif margin_type in ["top", "t"]:
            margin_type += "-top"

        elif margin_type in ["bottom", "bot", "b"]:
            margin_style += "-bottom"

        margin_style += ": 5px;\n"

        out += [margin_style]

    out += ["}\n"]

    return out


def choose_margin(current_user, selector, icon_name, **kwargs):
    if selector in ["custom-new-workspace", "custom-power"]:
        kwargs["margin"] = "right"

    elif selector == "pulseaudio":
        kwargs["margin"] = "left"

    return generic_icon_style(current_user, selector, icon_name, **kwargs)


selectors_icons = [
    "custom-power",
    "bluetooth",
    "network",
    "workspaces button",
    "workspaces button.active",
    "workspaces button.urgent",
    "custom-new-workspace",
    "pulseaudio",
    "pulseaudio.muted",
]

icon_names = [
    "logout",
    "bluetooth",
    "wifiworkspace-other",
    "workspace-current",
    "workspace-special",
    "new-workspace",
    "audio",
    "audio-muted",
]


def generate_css(current_user) -> str:
    with open("install_resources/css_beginning.txt", "r") as css_file:
        file_beginning = css_file.readlines()

    for selector, icon_name in zip(selectors_icons, icon_names):
        inactive_icon = choose_margin(current_user, selector, icon_name, hover=False)
        active_icon = generic_icon_style(current_user, selector, icon_name, hover=True)

        file_beginning += inactive_icon + ["\n"] + active_icon + ["\n"]

    with open("install_resources/css_ending.txt", "r") as ending_file:
        file_beginning += ending_file.readlines()

    return "".join(file_beginning)
