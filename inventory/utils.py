import os
import sys


def stock_image_path(instance, filename):
    return ".".join((instance.code, filename.split(".")[-1]))
