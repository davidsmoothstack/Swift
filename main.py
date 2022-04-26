import logging
import os

import log_config


if __name__ == "__main__":
    try:
        log_config.init()
        logging.info("Hello world")
    except:
        logging.exception("")
