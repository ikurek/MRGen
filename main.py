import argparse

from clint.textui import puts, colored
from pyfiglet import Figlet

from service.config_service import ConfigService
from service.git_service import GitService
from service.jira_service import JiraService
from service.path_service import PathService
from validation import git_validation, path_validation, jira_validation

args: argparse.Namespace

figlet = Figlet(font='slant')
path_service: PathService
config_service: ConfigService
git_service: GitService
jira_service: JiraService


def main():
    print(figlet.renderText('HLDP MR GEN'))
    parse_args()
    init()
    puts(colored.blue('Validating filesystem path'))
    path_validation.validate_path(path_service)
    puts(colored.blue('Validating git configuration'))
    git_validation.validate_git(git_service)
    puts(colored.blue('Validating JIRA connection'))
    jira_validation.validate_jira_connection(config_service, jira_service)


def parse_args():
    global args
    argument_parser = argparse.ArgumentParser(description='Generate merge request for HLDP GitLab repositories')
    argument_parser.add_argument('-p', '--path', action='store', type=str, help='Path of git repo')
    argument_parser.add_argument('-t', '--target', action='store', type=str, help='Target branch to merge into')
    args = argument_parser.parse_args()


def init():
    global path_service, git_service, jira_service, config_service
    path_service = PathService(args)
    config_service = ConfigService()
    git_service = GitService(path_service.path, args)
    jira_service = JiraService()


if __name__ == "__main__":
    main()
