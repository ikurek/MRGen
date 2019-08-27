from git import Repo


def is_git_repo(path):
    try:
        _ = Repo(path).git_dir
        return True
    except:
        return False


def has_git_remote(path):
    return len(Repo(path).remotes) > 0


def get_remote(path):
    return Repo(path).remotes.origin.url


def get_branch(path):
    return Repo(path).active_branch.name
