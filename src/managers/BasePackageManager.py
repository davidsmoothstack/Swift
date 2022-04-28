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
        """Checks if the package already exists on the system"""
        pass

    @abstractmethod
    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        pass

    @abstractmethod
    def update_repositores(self):
        """Update repositories before installing packages"""
        pass

    def post_check(self, package_name: str):
        """Runs a check after package is installed"""
        postInstall = self.yaml_config.postInstallTest
        result = shell(postInstall.command)

        if result.isSuccess == False:
            raise Exception(f"Error installing {package_name}")

        logging.info(f"{package_name} passed all regression tests")

    def auto_update(self, package_name):
        """Checks if a package is installed. If it's installed it upgrades it. If it's not, it installs the latest version
        Runs a post check on the installed package to make sure it's functional
        """
        self.update_repositores()

        if self.is_installed(package_name):
            self.upgrade_pipeline(package_name)
            return

        self.install_pipeline(package_name)

    def upgrade_pipeline(self, package_name):
        logging.info(
            f"Package '{package_name}' has been detected. Upgrading package...")
        self.upgrade_package(package_name)

        logging.info("Running post install actions...")
        self.post_check(package_name)

    def install_pipeline(self, package_name):
        logging.info(
            f"Package: '{package_name}' is not installed. Installing now...")
        self.install_package(package_name)

        logging.info("Running post install actions...")
        self.post_check(package_name)
