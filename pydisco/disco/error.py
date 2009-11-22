class DiscoError(Exception):
    pass

class JobException(DiscoError):
    def __init__(self, error, master=None, jobname=None):
        self.error   = error
        self.master  = master
        self.jobname = jobname

    def __str__(self):
        return "Job %s/%s failed: %s" % (self.master, self.jobname, self.error)

class CommException(DiscoError):
    def __init__(self, msg, url = ""):
        self.msg = msg
        self.url = url

    def __str__(self):
        return "HTTP exception (%s): %s" % (self.url, self.msg)
