import logging
import log_config
from util.manager_factory import PackageManagerType, get_package_manager

if __name__ == "__main__":
    try:
        log_config.init()

        manager = get_package_manager(PackageManagerType.APT)
        manager.install_package("docker")
    except:
        logging.exception("")
