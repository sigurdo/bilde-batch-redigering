#!/usr/bin/python3

import argparse
import inspect
import os
import subprocess
import time
import datetime

import exif


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


def rename_from_exif():
    for root, _dirs, files in os.walk("images", topdown=False):
        for filename in files:
            if filename == ".gitkeep":
                continue
            with open(os.path.join(root, filename), "rb") as image_file:
                image = exif.Image(image_file)
                time = datetime.datetime.strptime(
                    image.datetime_original, exif.DATETIME_STR_FORMAT
                )
                timestamp = time.strftime(r"%Y%m%d_%H%M%S")
                filename_new = f"{timestamp}_{filename}"
            os.rename(os.path.join(root, filename), os.path.join(root, filename_new))


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    for parameter in inspect.signature(rename_from_exif).parameters:
        argument_parser.add_argument(parameter)
    arguments = argument_parser.parse_args()
    rename_from_exif(**vars(arguments))
