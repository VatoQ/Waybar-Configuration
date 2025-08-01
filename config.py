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


class Config:
    def __new__(cls):
        raise TypeError(f"{cls.__name__} cannot be instantiated")

    TARGET_PATH:str = ""

    DAEMON_DIR:str = "popup_manager"

    EXISTS_STATUS:int = 0

    DOES_NOT_EXIST_STATUS:int = 1

    @classmethod
    def set_target_path(cls, current_user:str):
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

        cls.TARGET_PATH = f"/home/{current_user}/.config/waybar"
