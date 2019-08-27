import sys
import path_service
import git_service
from pyfiglet import Figlet
from clint.textui import puts, indent, colored

figlet = Figlet(font='slant')


def main():
    print(figlet.renderText('HLDP MR GEN'))
    path = path_service.get_path()
    with indent(4, '->'):
        puts(colored.blue('Validating files'))
        validate_path(path)
        validate_repository(path)
        validate_branch(path)
        validate_remote(path)


def validate_path(path):
    with indent(8, ''):
        if path is None:
            puts(colored.red('No path provided'))
            sys.exit()
        elif not path_service.is_pathname_valid(path):
            puts(colored.red('Invalid path provided'))
            sys.exit()
        else:
            puts(colored.green('Running in ' + path))

def validate_repository(path):
    with indent(8, ''):
        if not git_service.is_git_repo(path):
            puts(colored.red('Not a git repository'))
            sys.exit()
        else:
            puts(colored.green('Git repository configured'))

def validate_remote(path):
    with indent(8, ''):
        if not git_service.has_git_remote(path):
            puts(colored.red('No remote attached'))
            sys.exit()
        else:
            puts(colored.green('Attached to remote ' + git_service.get_remote(path)))


def validate_branch(path):
    with indent(8, ''):
        if git_service.get_branch(path) is None:
            puts(colored.red('No active branch inside repository'))
            sys.exit()
        elif not path_service.is_pathname_valid(path):
            puts(colored.red('Invalid path provided'))
            sys.exit()
        else:
            puts(colored.green('Running in ' + path))


if __name__ == "__main__":
    main()
