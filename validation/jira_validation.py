import sys

from clint.textui import colored, puts, indent


def validate_jira_connection(config_service, jira_service):
    jira_user = config_service.get_jira_user()
    jira_host = config_service.get_jira_host()
    validate_jira_login(jira_host, jira_user, jira_service)


def validate_jira_login(jira_host, jira_user, jira_service):
    with indent(4, '->'):
        if not jira_service.connect(jira_host, jira_user):
            puts(colored.red('Could not connect to JIRA, check Your credentials'))
            sys.exit()
        else:
            puts(colored.green('Authenticated in ' + jira_host))
            puts(colored.green(
                'Connected to JIRA as ' + jira_service.get_jira_name() + '(' + jira_service.get_jira_username() + ')'))
