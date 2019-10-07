import sys

from clint.textui import colored, puts, indent


def validate_git(git_service):
    validate_repository(git_service)
    validate_branch(git_service)
    validate_remote(git_service)


def validate_repository(git_service):
    with indent(4, '->'):
        if not git_service.is_git_repo():
            puts(colored.red('Not a git repository'))
            sys.exit()
        else:
            puts(colored.green('Git repository configured'))


def validate_remote(git_service):
    with indent(4, '->'):
        if not git_service.has_git_remote():
            puts(colored.red('No remote attached'))
            sys.exit()
        else:
            puts(colored.green('Attached to remote ' + git_service.get_remote()))


def validate_branch(git_service):
    with indent(4, '->'):
        if git_service.get_current_branch() is None:
            puts(colored.red('No active branch inside repository'))
            sys.exit()
        else:
            puts(colored.green('Selected branch ' + git_service.get_current_branch()))
