class SimpleJiraIssue:
    key: str
    summary: str
    url: str

    def __init__(self, key, summary, url):
        self.key = key
        self.summary = summary
        self.url = url
