import configparser
import os
from threading import Thread

import sublime
import sublime_plugin

try:
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    from .venvrunner import ConfigHandler, commands
except Exception as e:
    from venvrunner import ConfigHandler, commands

configfile = None
valid_exts = [".py", ".pyw"]
required_sections = ['system', 'enviroment']
required_options = {'system': ['os', 'pythoncall'],
                    'enviroment': ['path']}


def handle_config():
    config = configparser.ConfigParser()
    config.read(configfile)

    return config


def config_is_valid():
    config = handle_config()
    all_ok = True
    results = []

    win = sublime.active_window()
    panel = win.create_output_panel("vrunner")
    panel.set_read_only(False)

    def append_panel(typ, val):
        panel.run_command("append", {"characters": "VRunner: The {0} {1} is missing\n".format(typ, val)})

    for section in required_sections:
        if not config.has_section(section):
            all_ok = False if all_ok == True else False
            append_panel('section', section)
        else:
            for option in required_options[section]:
                if not config.has_option(section, option):
                    all_ok = False if all_ok == True else False
                    append_panel('option', "{0}/{1}".format(section, option))

    panel.set_read_only(True)

    return all_ok


def build_command(target):
    config = handle_config()
    activate = None
    args = None

    # system options
    sys_os = config["system"]["os"]
    pycall = config["system"]["pythoncall"]

    # enviroment options
    venv_path = config["enviroment"]["path"]

    # check ig exist extra args
    if config.has_section("args"):
        args = config["args"]
        args = [args[x] for x in args]
        args = " ".join(args)
    else:
        args = ""

    # Scripts directory (virtualenv)
    scripts = os.path.join(venv_path, "Scripts")

    # Directory of target file
    target_dir = os.path.dirname(target)

    # Filename of target
    target_filename = os.path.basename(target)

    base_cmd = commands[sys_os]

    part = base_cmd.format(scripts=scripts,
                           target_dir=target_dir,
                           pycall=pycall,
                           target_filename=target_filename,
                           args=args)

    return part


def execute(target):
    command = build_command(target)
    t = Thread(target=lambda: os.system(command))
    t.start()


class VenvrunnerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global configfile
        target_file = self.view.file_name()
        target_ext = os.path.splitext(target_file)[1]

        if target_ext in valid_exts:
            # If target its a Python file
            config_handler = ConfigHandler(target_file, "vrunner.ini")
            configfile = config_handler.get_config_file()

            if configfile:
                # If existe config file in project tree
                if config_is_valid():
                    # If config file hace valid struc
                    execute(target_file)
                else:
                    win = sublime.active_window()
                    win.run_command('show_panel', {"panel": "output.vrunner"})
