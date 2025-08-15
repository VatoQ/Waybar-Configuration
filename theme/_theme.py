from config import Config


theme_data:dict[str, dict[str, str]] = {
    Config.LIGHT: {
        Config.BACKGROUND: "rgba(100, 119, 179, 0.25)",
        Config.GROUP: "rgba(0, 119, 179, 0.5)",
    },
    Config.MEDIUM: {
        Config.BACKGROUND: "rgba(75, 89, 134, 0.25)",
        Config.GROUP: "rgba(0, 89, 134, 0.5)",
    },
    Config.DARK: {
        Config.BACKGROUND: "rgba(50, 60, 90, 0.35)",
        Config.GROUP: "rgba(0, 60, 90, 0.5)",
    },
}
