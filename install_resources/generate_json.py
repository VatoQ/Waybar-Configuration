def generate_json(current_user: str) -> str:
    with open("install_resources/json_content.txt", "r") as json_file:
        lines = json_file.readlines()

    return "".join(lines)
