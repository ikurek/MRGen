from service.git_service import GitService
from service.jira_service import JiraService
from service.merge_request_markdown_service import MergeRequestMarkdownService
from ui import merge_request_ui


class MergeRequestService:
    git_service: GitService
    jira_service: JiraService
    issue_keys: list
    issues: list

    def __init__(self, git_service, jira_service):
        self.git_service = git_service
        self.jira_service = jira_service

    def get_issue_keys(self):
        self.issue_keys = self.git_service.get_jira_issue_codes_from_commits()
        merge_request_ui.print_jira_issue_keys(self.issue_keys)

    def get_issues_by_keys(self):
        self.issues = list()
        for issue in self.jira_service.generate_issues_by_issue_keys(self.issue_keys):
            self.issues.append(issue)
            merge_request_ui.print_simple_jira_issue(issue)

    def build_merge_request_message(self):
        markdown_service = MergeRequestMarkdownService()
        markdown_service.add_header_addressed_issues()
        for issue in self.issues:
            markdown_service.add_issue_bullet_point(issue)
        print(markdown_service.get_message())
