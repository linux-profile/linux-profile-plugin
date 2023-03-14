from linux_profile.main import BuildCommand
from linux_profile.base.command import BaseCommand
from linux_profile_plugin.commands import HelloWorld


class ArgsCommand(BaseCommand):

    def __init__(self, parser):
        super().__init__(parser)

        # "hello" command launcher.
        self.setup_hello()

    def setup_hello(self):
        """Argument loading method for the new command.
        """
        self.cmd_hello = self.subparsers.add_parser('hello', help="My custom command")
        self.cmd_hello = self.cmd_hello.add_argument_group('Usage: linuxp hello [OPTIONS]')
        self.cmd_hello.add_argument('--message')


class Build(BuildCommand):

    base_command = ArgsCommand

    def setup(self) -> str:
        """Method for initializing custom commands.
        """
        self.command.cmd_hello.set_defaults(exec=HelloWorld)


def main():
    Build()


if __name__ == '__main__':
    main()
