#!/bin/python

from config import Config

class PopupDaemon:
    def __new__(cls) -> None:
        raise TypeError(f"{cls.__name__} cannot be instantiated.")

    @classmethod
    def query_window(cls, window_name:str) -> None:
        pass

    @classmethod
    def move_to_special(cls, window_name:str) -> None:
        pass

    @classmethod
    def move_from_special(cls, window_name:str) -> None:
        pass


def main_loop():
    window_names_dict = {
        "blueman-manager": "blueman-manager",
        "network": "nm-connection-editor",
        "pavucontrol": "org.pulseaudio.pavucontrol",
        "calendar": "org.gnome.Calendar",
    }

    window_names = [value for key, value in window_names_dict.items()]

    



if __name__ == "__main__":
    main_loop()
