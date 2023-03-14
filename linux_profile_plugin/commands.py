from linux_profile.base.command import Command


class HelloWorld(Command):

    def execute(self):
        """Method for initializing custom commands.
        """
        print("Hello World!", (self.arguments.message or ""))
