import logging
import os

from models.ShellResult import ShellResult


def shell(command) -> ShellResult:
    """Runs a shell command. Returns the status code"""
    logging.debug(f"Executing shell command: {command}")
    status_code = os.system(command)
    isSuccess = status_code == 0

    return ShellResult(isSuccess, status_code)
