import sys

from clint.textui import colored, puts, indent

from model.simple_jira_issue import SimpleJiraIssue


def print_jira_issue_keys(issue_keys: list):
    with indent(4, '->'):
        if len(issue_keys) == 0:
            puts(colored.green('No issue keys found in commit messages'))
            sys.exit()
        else:
            puts(colored.green('Found ' + len(issue_keys).__str__() + ' issues'))


def print_simple_jira_issue(simple_jira_issue: SimpleJiraIssue):
    with indent(4, '->'):
        puts(colored.green('[' + simple_jira_issue.key + '] ' + simple_jira_issue.summary))
