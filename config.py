class Config:
    def __new__(cls):
        raise TypeError(f"{cls.__name__} cannot be instantiated")

    TARGET_PATH = ""

    DAEMON_DIR = "popup_manager"

    EXISTS_STATUS = 0

    DOES_NOT_EXIST_STATUS = 1

    @classmethod
    def set_target_path(cls, current_user):
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
