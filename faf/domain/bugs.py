class BugReportTarget:
    def __init__(self, name, url=None, ref=None):
        self.name = name
        self.url = url
        self.ref = ref

    @property
    def id(self):
        return "{}/tree/{}".format(self.name, self.ref)

    def __eq__(self, other):
        if not isinstance(other, BugReportTarget):
            return False
        return other.name == self.name and other.ref == self.ref

    def __str__(self):
        return "BugReportTarget({name},{url},{ref})".format(
            **dict(name=self.name,
                   url=self.url,
                   ref=self.ref)
        )


class BugReport:
    """
    Represents a bug report
    """
    def __init__(self,
                 title,
                 id=None,
                 target=BugReportTarget(name='FAForever/client'),
                 automatic=False,
                 description="",
                 log="",
                 traceback="",
                 create_time=None,
                 update_time=None):
        self.title = title
        self.id = id
        self.target = target
        self.automatic = automatic
        self.description = description
        self.log = log
        self.traceback = traceback
        self.create_time, self.update_time = create_time, update_time

    def __str__(self):
        return "BugReport({id},{title},{target},{automatic})".format(
            **dict(id=self.id,
                   title=self.title,
                   target=self.target,
                   automatic=self.automatic)
        )
