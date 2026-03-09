class Job:
    def __init__(self, title, company, url, description):
        self.title = title
        self.company = company
        self.url = url
        self.description = description

    def __repr__(self):
        return f"{self.title} - {self.company}"