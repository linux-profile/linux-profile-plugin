from linux_profile.main import BuildCommand
from linux_profile.base.command import BaseCommand
from linux_profile_plugin.commands import HelloWorld, Explore


class ArgsCommand(BaseCommand):

    def __init__(self, parser):
        super().__init__(parser)

        # "hello" command launcher.
        self.setup_hello()

        # "explore" command launcher.
        self.setup_explore()

    def setup_hello(self):
        """Argument loading method for the new command.
        """
        self.cmd_hello = self.subparsers.add_parser('hello', help="My custom command.")
        self.cmd_hello = self.cmd_hello.add_argument_group('Usage: linuxp_plugin hello [OPTIONS]')
        self.cmd_hello.add_argument('--message')

    def setup_explore(self):
        """Argument loading method for the new command.
        """
        self.cmd_explore = self.subparsers.add_parser('explore', help="This command shows some settings.")
        self.cmd_explore = self.cmd_explore.add_argument_group('Usage: linuxp_plugin explore [OPTIONS]')


class Build(BuildCommand):

    base_command = ArgsCommand

    def setup(self) -> str:
        """Method for initializing custom commands.
        """
        self.command.cmd_hello.set_defaults(exec=HelloWorld)
        self.command.cmd_explore.set_defaults(exec=Explore)


def main():
    Build()


if __name__ == '__main__':
    main()
