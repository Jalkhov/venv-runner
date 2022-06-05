commands = {"windows": ("cmd /k "
                        "\"cd {scripts} "
                        "& activate.bat "
                        "& cd {target_dir} "
                        "& {pycall} {target_filename} {args}\"")
            }
