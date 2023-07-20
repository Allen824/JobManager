class Job:
    def __init__(self, job_id, name, completed):
        self.job_id = job_id
        self.name = name
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"Task {self.job_id}: {self.name} ({status})"
