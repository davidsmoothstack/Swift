import logging
from models.AptPackageManager import AptPackageManager

import log_config


if __name__ == "__main__":
    try:
        test = AptPackageManager()
    except:
        logging.exception("")
