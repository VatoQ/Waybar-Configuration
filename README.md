# Waybar Configuration

![example screenshot](./screenshots/example.png)

Configuring waybar to look a little more modern. There is also a
daemon to manage the applets launched by some of the buttons.

## Required packages

- waybar
- pavucontrol
- bluez
- gnome-calendar
- nm-connection-editor

## Recommended packages

- bluez-utils

## Installation

You probably want to backup your existing waybar config, as
the install script will delete `~/.config/waybar/*` without asking.
In a directory that is not `~/.config/waybar`, run:

```
git clone https://github.com/VatoQ/Waybar-Configuration.git
cd Waybar-Configuration
./install.py
```

### Options for install command

- `--font_size`: integer
