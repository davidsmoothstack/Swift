from abc import ABC, abstractmethod
import logging

from util.shell import shell


class BasePackageManager(ABC):
    def __init__(self, yaml_config=None):
        super().__init__()
        self.yaml_config = yaml_config

    @abstractmethod
    def install_package(self, package_name: str):
        """Installs a package"""
        pass

    @abstractmethod
    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        pass

    @abstractmethod
    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        pass

    def post_install(self, package_name: str):
        """Runs a check after package is installed"""
        postInstall = self.yaml_config.postInstallTest

        result = shell(postInstall.command)

        if result.isSuccess == False:
            raise Exception(f"Error installing {package_name}")

        return result.isSuccess

    def auto_update(self, package_name):
        if self.is_installed(package_name) == False:
            logging.info(
                f"Package: '{package_name}' is not installed. Installing now...")
            self.install_package(package_name)

            logging.info("Running post install actions...")
            self.post_install(package_name)
            return

        logging.info(
            f"Package '{package_name}' has been detected. Upgrading package...")
        self.upgrade_package(package_name)

        logging.info("Running post install actions...")
        self.post_install(package_name)
