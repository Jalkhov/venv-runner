import os


def get_filenames(path, filename):
    """Yield full filepath for filename in each directory in and above path"""
    path_list = []
    while True:
        path_list.append(os.path.join(path, filename))
        newpath = os.path.dirname(path)
        if path == newpath:
            break
        path = newpath
    return path_list


class ConfigHandler(object):
    def __init__(self, filepath, conf_filename='.editorconfig'):
        """Create EditorConfigHandler for matching given filepath"""
        self.filepath = filepath
        self.conf_filename = conf_filename

    def get_config_file(self):
        path, filename = os.path.split(self.filepath)
        conf_files = get_filenames(path, self.conf_filename)

        for file in conf_files:
            if os.path.isfile(file):
                # Just get first occurrence
                return file
                break
