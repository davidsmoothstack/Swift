import logging
import log_config
from managers.PackageManagerFactory import (PackageManagerType,
                                            get_package_manager)

if __name__ == "__main__":
    try:
        manager = get_package_manager(PackageManagerType.APT)
        manager.install_package("docker")
    except:
        logging.exception("")
