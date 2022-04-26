import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ShellResult():
    isSuccess: bool
    statusCode: int


def shell(command) -> ShellResult:
    """Runs a shell command. Returns the status code"""
    status_code = os.system(command)
    isSuccess = status_code == 0

    return ShellResult(isSuccess, status_code)
