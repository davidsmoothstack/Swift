from datetime import datetime
import logging
import os
import sys

log_directory = "logs"
logging_format = "[%(asctime)s] %(message)s"
logging_date_format = "%b %d %Y %X"


def check_base_dir(log_directory):
    """Checks if the base logging directory exists. If not this function creates it"""
    if os.path.isdir(log_directory) == False:
        os.mkdir(log_directory)


def generate_logfile_path(root_directory):
    """Generates a complete path for a logfile"""

    parent_directory = datetime.now().strftime("%b %d %Y")
    logfile = f"{datetime.now().strftime('%X')}.txt"
    complete_path = f"{root_directory}/{parent_directory}"

    if os.path.isdir(complete_path) == False:
        os.mkdir(complete_path)

    return f"{complete_path}/{logfile}"


def init():
    check_base_dir(log_directory)

    log_file = generate_logfile_path(log_directory)

    logging.basicConfig(
        level=logging.INFO,
        format=logging_format,
        datefmt=logging_date_format,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
