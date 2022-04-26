from abc import ABC, abstractmethod


class IPackageManager(ABC):
    @abstractmethod
    def install_package(self, package_name: str):
        """Installs a package"""
        pass

    @abstractmethod
    def post_check(self, package_name: str):
        """Runs a check after package is installed"""
        pass

    @abstractmethod
    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        pass

    @abstractmethod
    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        pass
