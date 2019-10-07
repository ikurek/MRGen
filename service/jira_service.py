from jira import JIRA

from model.simple_jira_issue import SimpleJiraIssue
from model.user_credentials import UserCredentials


class JiraService:
    jira: JIRA
    host: str

    def connect(self, host: str, user: UserCredentials) -> bool:
        try:
            self.host = host
            self.jira = JIRA(server=self.host, basic_auth=(user.username, user.password))
            return True
        except Exception:
            return False

    def get_jira_name(self) -> str:
        return self.jira.myself()['displayName']

    def get_jira_email(self) -> str:
        return self.jira.myself()['emailAddress']

    def generate_issues_by_issue_keys(self, issue_keys):
        for issue_key in issue_keys:
            jira_issue = self.jira.issue(id=issue_key)
            jira_issue_browser_url = self.host + '/browse/' + issue_key
            jira_issue_summary = jira_issue.raw['fields']['summary']
            yield SimpleJiraIssue(issue_key, jira_issue_summary, jira_issue_browser_url)
