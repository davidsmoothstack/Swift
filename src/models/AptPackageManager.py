from models.IPackageManager import IPackageManager
from shell import shell


class AptPackageManager(IPackageManager):
    def install_package(self, package_name: str):
        """Installs a package"""
        return shell(f"sudo apt install -y {package_name}")

    def post_install(self, package_name: str):
        """Runs a check after package is installed"""
        pass

    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        return shell(f"sudo apt-cache show {package_name}")

    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        return shell(f"sudo apt install --only-upgrade {package_name}")
