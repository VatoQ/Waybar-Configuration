
def generic_icon_style(current_user:str, selector:str, icon_name:str, **kwargs:bool|str):
    """
    Generates css to style an icon for a specified selector.

    can also add the hover selector if specified in `**kwargs` viw `hover = True`

    Parameters
    ----------
    current_user : str
        current user to ensure correct path to icons.
    selector : str
        the selector corresponding to the waybar element to be styled.
    icon_name : str
        name of the icon for the specified selector.
    """
    out = [f"#{selector}", "\n", "{\n"]

    if kwargs.get("hover", None) and kwargs.get("hover") is True:
        out[0] += ":hover"
        icon_name += "-hover"
    else:
        icon_name += "-inactive"

    image_url = f"/home/{current_user}/.config/waybar/icons/{icon_name}.svg"

    image_style = f"    background-image: url('{image_url}');\n"

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


def choose_margin(current_user:str, selector:str, icon_name:str, **kwargs:bool|str):
    """
    Determins if a margin should be applied to the style.

    This puts a margin on icons that are at the borders of selections.

    Parameters
    ----------
    current_user : str
        current user to ensure correct path to icons.
    selector : str
        the selector corresponding to the waybar element to be styled.
    icon_name : str
        name of the icon for the specified selector.
    """
    if selector in ["custom-new-workspace", "custom-power"]:
        kwargs["margin"] = "right"

    elif selector in ["pulseaudio", "network", "custom-menu"]:
        kwargs["margin"] = "left"

    return generic_icon_style(current_user, selector, icon_name, **kwargs)


selectors_icons = [
    "custom-menu",
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
    "menu",
    "logout",
    "bluetooth",
    "wifi",
    "workspace-other",
    "workspace-current",
    "workspace-special",
    "new-workspace",
    "audio",
    "audio-muted",
]
global_selector = [
    "*\n",
    "{\n",
    "    border: none;\n",
    '    font-family: "Adwaita Sans", Roboto, Arial, sans-serif;\n',
    "    color: #ffffff;\n",
    "    border-radius: 25px;\n",
]


button_selector = [
    "#custom-power,\n",
    "#custom-new-workspace,\n",
    "#custom-menu,\n",
    "#workspaces button,\n",
    "#network,\n",
    "#bluetooth,\n",
    "#pulseaudio,\n",
    "#workspaces,\n",
    "#workspaces button\n{\n",
]

button_rest = [
    "    background-position: center;\n",
    "    background-repeat: no-repeat;\n",
    "    background-size: contain;\n",
    "    margin: 0px;\n",
    "    transition: background-image 0.3s ease-in-out;\n",
    "}\n\n",
]


def generate_css(current_user:str, **kwargs:int|str) -> str:
    """
    Generates the css styling for waybar.

    Some styling contains absolute paths to icons.
    These paths must be correctly generated at each installation.
    This is why css is generated and not copied.

    Parameters
    ----------
    current_user : str
        current user to ensure correct installation.

    Returns
    -------
    str
        content of the css file as a string.
    """
    with open("install_resources/css_beginning.txt", "r") as css_file:
        file_beginning = css_file.readlines()

    font_size = 30
    if kwargs.get("font_size", None):
        font_size = kwargs["font_size"]

    assert isinstance(font_size, int)
    prefix = global_selector + [f"    font-size: {int(0.5 * font_size)}px;\n", "}\n\n"]

    file_beginning += prefix

    button_style = button_selector + [f"    font-size: {font_size}px;\n"] + button_rest

    file_beginning += button_style

    for selector, icon_name in zip(selectors_icons, icon_names):
        inactive_icon = choose_margin(current_user, selector, icon_name, hover=False)
        active_icon = generic_icon_style(current_user, selector, icon_name, hover=True)

        file_beginning += inactive_icon + ["\n"] + active_icon + ["\n"]

    with open("install_resources/css_ending.txt", "r") as ending_file:
        file_beginning += ending_file.readlines()

    return "".join(file_beginning)
