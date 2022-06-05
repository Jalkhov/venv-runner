# Venv Runner

Run Python scripts from Sublime Text using a existing virtual enviroment.


## Install

Install `Venv Runner` with [Package Control](https://packagecontrol.io) and restart Sublime.


## Getting started

### Supported configs

- **system (required)**
  - **os:** Operative system of the machine (For now, just windows is supported)
  - **pythoncall:** How do you call python files
- **enviroment (required)**
  - **path:** Virtual enviroment container folder
- **args (optional)**
  - Arguments for pass to the file

### Example file

```ini
[system]
os = windows
pythoncall = python; python3 or py3

[enviroment]
path = C:\path\to\your\enviroments\env-sample

[args]
path = path/to/the/sample/file
number = 34
name = "Jhon Doe"
; Args with spaces must be inside cuotes
```

Once you have your `vrunner.ini` file set up, use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>-</kbd> on Linux/Windows or <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>-</kbd> on macOS to run the script, or right click somewhere in the open file and press **VRunner**.

# Advice

Tested only on Windows. Do you want to help me by testing it on other platforms? :)

# TODO

- [ ] Autodetect operative system (system/os config)
- [ ] Add support for Linux bases OS
- [ ] Add support for MacOS
