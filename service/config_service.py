import config
from model.user_credentials import UserCredentials


class ConfigService:

    def get_jira_host(self) -> str:
        return config.jira['host']

    def get_jira_user(self) -> UserCredentials:
        return UserCredentials(config.jira['username'], config.jira['password'])
