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


def delete_timestamps():
    for root, _dirs, files in os.walk("images", topdown=False):
        for filename in files:
            filename_new = re.sub(r"\d\d\d\d\d\d\d\d_\d\d\d\d\d\d_", "", filename)
            os.rename(os.path.join(root, filename), os.path.join(root, filename_new))


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    for parameter in inspect.signature(delete_timestamps).parameters:
        argument_parser.add_argument(parameter)
    arguments = argument_parser.parse_args()
    delete_timestamps(**vars(arguments))
