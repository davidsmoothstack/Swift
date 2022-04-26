class IPackageManager():
    def install_package(self, package_name: str):
        """Installs a package"""
        pass

    def post_check(self, package_name: str):
        """Runs a check after package is installed"""
        pass

    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        pass

    def upgrade_package(self, package_name: str):
        pass
