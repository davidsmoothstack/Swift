import logging
import log_config
from util.manager_factory import get_package_manager
from util.yaml_parser import read_yaml


if __name__ == "__main__":
    try:
        log_config.init()

        yml = read_yaml("packages.yml")

        for package_config in yml.packages:
            try:
                manager = get_package_manager(package_config)
                manager.execute(package_config.name)
            except:
                logging.error(f"Error installing {package_config.name}")
                continue

    except:
        logging.exception("")
