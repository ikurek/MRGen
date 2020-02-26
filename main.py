import argparse

from clint.textui import puts, colored
from pyfiglet import Figlet

from service.config_service import ConfigService
from service.git_service import GitService
from service.jira_service import JiraService
from service.merge_request_service import MergeRequestService
from service.path_service import PathService
from ui import git_validation, path_validation, jira_validation

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
    puts(colored.blue('Searching for issue keys'))
    merge_request_service = MergeRequestService(git_service, jira_service)
    merge_request_service.get_issue_keys()
    puts(colored.blue('Getting issue info from JIRA'))
    merge_request_service.get_issues_by_keys()
    puts(colored.blue('Building markdown message'))
    merge_request_service.build_merge_request_message()


def parse_args():
    global args
    argument_parser = argparse.ArgumentParser(description='Generate merge request for HLDP GitLab repositories')
    argument_parser.add_argument('-p', '--path', action='store', type=str, help='Path of git repo')
    argument_parser.add_argument('-s', '--source', action='store', type=str, help='Source branch to be merged')
    argument_parser.add_argument('-t', '--target', action='store', type=str, help='Target branch to merge into')
    argument_parser.add_argument('-g', '--git-pull', action='store_true',
                                 help='Pull changes from target/source branches before creating MR')
    args = argument_parser.parse_args()


def init():
    global path_service, git_service, jira_service, config_service, gitlab_service
    path_service = PathService(args)
    config_service = ConfigService()
    git_service = GitService(path_service.path, args)
    jira_service = JiraService()


if __name__ == "__main__":
    main()
