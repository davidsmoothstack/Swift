from managers.BasePackageManager import BasePackageManager
from util.shell import shell


class YumPackageManager(BasePackageManager):
    def update_repositores(self):
        return shell("sudo yum update")

    def install_package(self, package_name: str):
        """Installs a package"""
        return shell(f"sudo yum install -y {package_name}")

    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        result = shell(f"yum list installed {package_name}")
        return result.isSuccess

    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        return shell(f"sudo yum update -y {package_name}")
