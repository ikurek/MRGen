from jira import JIRA

from model.user_credentials import UserCredentials


class JiraService:
    jira: JIRA

    def connect(self, host: str, user: UserCredentials) -> bool:
        try:
            self.jira = JIRA(server=host, basic_auth=(user.username, user.password))
            return True
        except Exception:
            return False

    def get_jira_name(self) -> str:
        return self.jira.myself()['displayName']

    def get_jira_username(self) -> str:
        return self.jira.myself()['name']
