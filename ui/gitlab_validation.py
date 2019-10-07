import sys

from clint.textui import colored, puts, indent


def validate_gitlab_connection(config_service, gitlab_service):
    gitlab_host = config_service.get_gitlab_host()
    gitlab_access_token = config_service.get_gitlab_access_token()
    validate_gitlab_login(gitlab_host, gitlab_access_token, gitlab_service)


def validate_gitlab_login(gitlab_host, gitlab_access_token, gitlab_service):
    with indent(4, '->'):
        if not gitlab_service.connect(gitlab_host, gitlab_access_token):
            puts(colored.red('Could not connect to GitLab, check Your credentials'))
            sys.exit()
        else:
            puts(colored.green('Authenticated in ' + gitlab_host))
            puts(colored.green(
                'Connected to GitLab as ' + gitlab_service.get_gitlab_name() + ' (' + gitlab_service.get_gitlab_email() + ')'))
