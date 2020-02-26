import sys

from clint.textui import colored, puts, indent


def validate_git(git_service):
    validate_repository(git_service)
    validate_branch(git_service)
    validate_remote(git_service)
    validate_branch_pull(git_service)
    validate_commits(git_service)


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
        if git_service.source_branch is None:
            puts(colored.red('No active branch inside repository'))
            sys.exit()
        else:
            puts(colored.green('Selected branch ' + git_service.source_branch))


def validate_commits(git_service):
    with indent(4, '->'):
        if len(list(git_service.generate_current_branch_commits())) == 0:
            puts(colored.red('No commits ahead of ' + git_service.target_branch))
            sys.exit()
        else:
            puts(colored.green('Commits ahead of ' + git_service.target_branch + ': ' +
                               len(list(git_service.generate_current_branch_commits())).__str__()))


def validate_branch_pull(git_service):
    with indent(4, '->'):
        if git_service.should_pull:
            puts(colored.white('Pulling branches (--git-pull flag is set)'))
            if not git_service.pull_target_branch():
                puts(colored.red('Could not pull target branch ' + git_service.target_branch))
                sys.exit()
            else:
                puts(colored.green('Pulled target branch ' + git_service.target_branch))

            if not git_service.pull_source_branch():
                puts(colored.red('Could not pull source branch ' + git_service.source_branch))
                sys.exit()
            else:
                puts(colored.green('Pulled source branch ' + git_service.source_branch))
