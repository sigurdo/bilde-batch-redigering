#!/usr/bin/python3

import argparse
import inspect
import os
import subprocess
import time
import re


def r(*path):
    """
    Takes a relative path from the directory of this python file and returns the absolute path.
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), *path)


def run_in_dir(directory, callable):
    cwd = os.getcwd()
    os.chdir(directory)
    result = callable()
    os.chdir(cwd)
    return result


def standardize_extensions():
    for root, _dirs, files in os.walk("images", topdown=False):
        for filename in files:
            for pattern, replacement in [
                (r".[Jj][Pp][Gg]$", ".jpg"),
                (r".[Jj][Pp][Ee][Gg]$", ".jpg"),
            ]:
                filename_new, num_subs = re.subn(pattern, replacement, filename)
                if num_subs >= 1:
                    os.rename(
                        os.path.join(root, filename), os.path.join(root, filename_new)
                    )
                    break


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    for parameter in inspect.signature(standardize_extensions).parameters:
        argument_parser.add_argument(parameter)
    arguments = argument_parser.parse_args()
    standardize_extensions(**vars(arguments))

    # 20231213_160435_Hurtigruta lys.JPG
