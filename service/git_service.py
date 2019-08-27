from git import Repo


class GitService:

    def __init__(self, path):
        self.path = path
        self.repo = Repo(path)

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

    def get_branch(self):
        return self.repo.active_branch.name
