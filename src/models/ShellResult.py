from dataclasses import dataclass


@dataclass(frozen=True)
class ShellResult():
    isSuccess: bool
    statusCode: int
