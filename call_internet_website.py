# Copyright(C] 2021 cGIfl300 <cgifl300@gmail.com>

from subprocess import run


def call_internet_website():
    """ If the script doesn't work, you should review the path of python interpreter below
    :return: a json object
    """
    shell_stdout = run("venv\\Scripts\\python.exe speedtest.py --json", shell=True, capture_output=True)
    shell_stdout = shell_stdout.stdout.decode()
    return shell_stdout
