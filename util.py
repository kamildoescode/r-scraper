import os

from fake_useragent import UserAgent


def gen_headers():
    return {
        'User-Agent': UserAgent().random
    }


def file_exists(path: str) -> bool:
    return os.path.exists(path)

def dir_create(path: str):
    """
    Check is path given is a directory that exists, if not create
    :param path: path to dir
    """

    if not os.path.isdir(path):
        os.mkdir(path)


def remove_file(path: str):
    """
    Remove file at the given path if exists
    :param path: filepath to be removed
    """

    if os.path.exists(path):
        os.remove(path)
