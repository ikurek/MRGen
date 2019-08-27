from clint.textui import puts, colored
from pyfiglet import Figlet

from service.config_service import ConfigService
from service.git_service import GitService
from service.jira_service import JiraService
from service.path_service import PathService
from validation import git_validation, path_validation, jira_validation

figlet = Figlet(font='slant')
path_service: PathService
config_service: ConfigService
git_service: GitService
jira_service: JiraService


def main():
    print(figlet.renderText('HLDP MR GEN'))
    init()
    puts(colored.blue('Validating filesystem path'))
    path_validation.validate_path(path_service)
    puts(colored.blue('Validating git configuration'))
    git_validation.validate_git(git_service)
    puts(colored.blue('Validating JIRA connection'))
    jira_validation.validate_jira_connection(config_service, jira_service)


def init():
    global path_service, git_service, jira_service, config_service
    path_service = PathService()
    config_service = ConfigService()
    git_service = GitService(path_service.path)
    jira_service = JiraService()


if __name__ == "__main__":
    main()
