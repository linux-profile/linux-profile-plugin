from linux_profile.base.settings import Settings
from linux_profile.base.command import Command


class HelloWorld(Command):

    def execute(self):
        """Method for initializing custom commands.
        """
        print("Hello World!", (self.arguments.message or ""))


class Explore(Command):

    def execute(self):
        """Method for initializing custom commands.
        """
        settings = Settings()
        configs = [
            "file_aliases",
            "file_bashrc",
            "path_config",
            "path_install",
            "path_profile",
            "path_temp",
            "file_config",
            "file_profile"]
        
        for config in configs:
            if hasattr(settings, config):
                print(f"{config}:".rjust(15), getattr(settings, config))
