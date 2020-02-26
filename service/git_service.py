import re

from git import Repo, Head


class GitService:
    repo: Repo
    target_branch: str
    source_branch: str
    should_pull: bool

    def __init__(self, path, args):
        self.path = path
        self.repo = Repo(path)
        self.parse_args(args)

    def parse_args(self, args):
        if args.target is not None:
            self.target_branch = args.target
        else:
            self.target_branch = self.get_default_target_branch()

        if args.source is not None:
            self.source_branch = args.source
        else:
            self.source_branch = self.get_current_branch()

        if args.git_pull is not None:
            self.should_pull = args.git_pull
        else:
            self.should_pull = False

    def is_git_repo(self):
        try:
            _ = self.repo.git_dir
            return True
        except:
            return False

    def has_git_remote(self):
        return len(self.repo.remotes) > 0

    def get_remote(self):
        return self.repo.remotes.origin.url

    def get_current_branch(self):
        return self.repo.active_branch.name

    def get_default_target_branch(self):
        return 'develop'

    def checkout_branch(self, branch):
        return self.repo.heads[branch].checkout

    def pull_target_branch(self):
        try:
            target_branch_reference: Head = self.checkout_branch(self.target_branch)
            target_branch_reference.repo.git.pull()
            return True
        except Exception:
            return False

    def pull_source_branch(self):
        try:
            source_branch_reference: Head = self.checkout_branch(self.source_branch)
            source_branch_reference.repo.git.pull()
            return True
        except Exception:
            return False

    def generate_current_branch_commits(self):
        develop_commits = list(self.repo.iter_commits(self.target_branch))
        current_commits = list(self.repo.iter_commits(self.source_branch))
        for commit in current_commits:
            if commit not in develop_commits:
                yield commit

    def get_jira_issue_codes_from_commits(self):
        issue_keys = list(set(self.generate_jira_issue_codes_from_commits()))
        issue_sorting_converter = lambda text: int(text) if text.isdigit() else text
        issue_sorting_key = lambda key: [issue_sorting_converter(c) for c in re.split('([0-9]+)', key)]
        issue_keys.sort(key=issue_sorting_key)
        return issue_keys

    def generate_jira_issue_codes_from_commits(self):
        source_branch_reference = self.checkout_branch(self.source_branch)
        commits = self.generate_current_branch_commits()
        for commit in commits:
            issue_key_tuple = re.search(r"\[([A-Za-z0-9-_]+)\]", commit.message)
            if issue_key_tuple is not None:
                for issue_key in issue_key_tuple.groups():
                    if '-' in issue_key:
                        yield issue_key
