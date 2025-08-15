from config import Config


theme_data:dict[str, dict[str, str]] = {
    Config.LIGHT: {
        Config.BACKGROUND: "rgba(100, 119, 179, 0.25)",
        Config.GROUP: "rgba(0, 119, 179, 0.6)",
    },
    Config.MEDIUM: {
        Config.BACKGROUND: "rgba(75, 79, 134, 0.25)",
        Config.GROUP: "rgba(0, 79, 134, 0.5)",
    },
    Config.DARK: {
        Config.BACKGROUND: "rgba(50, 45, 90, 0.35)",
        Config.GROUP: "rgba(0, 45, 90, 0.5)",
    },
}
