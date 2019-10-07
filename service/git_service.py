from git import Repo


class GitService:

    def __init__(self, path, args):
        self.path = path
        self.repo = Repo(path)
        if args.target is not None:
            self.target_branch = args.target
        else:
            self.target_branch = 'develop'

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

    def generate_current_branch_commits(self):
        develop_commits = list(self.repo.iter_commits(self.target_branch))
        current_commits = list(self.repo.iter_commits(self.get_current_branch()))
        for commit in current_commits:
            if commit not in develop_commits:
                yield commit
