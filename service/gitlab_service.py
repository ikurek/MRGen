from gitlab import Gitlab


class GitlabService:
    gl: Gitlab

    def connect(self, host, access_token):
        try:
            self.gl = Gitlab(host, private_token=access_token)
            self.gl.auth()
            return True
        except Exception as e:
            print(e)
            return False

    def get_gitlab_name(self):
        return self.gl.user.name

    def get_gitlab_email(self):
        return self.gl.user.email
