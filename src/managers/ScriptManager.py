import logging
from managers.BasePackageManager import BasePackageManager
from util.shell import shell
from pathlib import Path

class ScriptPackageManager(BasePackageManager):
    def update_repositores(self):
        return shell("sudo apt update")


    def install_package(self, package_name: str):
        """Installs a package"""
        script = Path(f"scripts/{self.yaml_config.manager.scriptName}").absolute()
        version = f"{self.yaml_config.manager.params.version}"

        return shell(f"{script} {version}")


    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        result = shell(f"sudo apt -qq list {package_name} | grep installed")
        return result.isSuccess


    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        return None
        # return shell(f"sudo apt install --only-upgrade {package_name}")
