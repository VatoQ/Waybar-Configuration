from config import Config


def generate_init(current_user: str, **kwargs) -> str:
    with open("install_resources/initialize_beginning.txt", "r") as py_file:
        file_beginning = py_file.readlines()

    json_path = f"out_path = '/home/{current_user}/.config/waybar/{Config.DAEMON_DIR}/pop_up_states.json'\n"

    dump_command = [
        "with open(out_path, 'w') as json_file:\n",
        "    json.dump(pop_up_states, json_file, indent=4)\n",
    ]

    file_beginning += [json_path] + dump_command

    return "".join(file_beginning)
