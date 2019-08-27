import sys

from clint.textui import colored, puts, indent


def validate_path(path_service):
    with indent(4, '->'):
        if path_service.path is None:
            puts(colored.red('No path provided'))
            sys.exit()
        elif not path_service.is_pathname_valid(path_service.path):
            puts(colored.red('Invalid path provided'))
            sys.exit()
        else:
            puts(colored.green('Running in ' + path_service.path))
