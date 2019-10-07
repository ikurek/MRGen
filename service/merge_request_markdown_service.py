from model.simple_jira_issue import SimpleJiraIssue


class MergeRequestMarkdownService:
    markdownContent: str

    def __init__(self):
        self.markdownContent = ''

    def add_header_addressed_issues(self, ):
        self.markdownContent = self.markdownContent + '### Addressed Issues\n'

    def add_issue_bullet_point(self, simple_jira_issue: SimpleJiraIssue):
        self.markdownContent = self.markdownContent + (
                    '* [[' + simple_jira_issue.key + '] ' + simple_jira_issue.summary + '](' + simple_jira_issue.url + ')\n')

    def get_message(self):
        return self.markdownContent
