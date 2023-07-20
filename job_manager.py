class JobManager:
    def __init__(self):
        self.jobs = []
        self.last_job_id = 0  # To keep track of the last assigned task ID

    def add_job(self, job):
        self.last_job_id += 1
        job.job_id = self.last_job_id
        self.jobs.append(job)

    def delete_job_by_id(self, job_id):
        for job in self.jobs:
            if job.job_id == job_id:
                self.jobs.remove(job)
                self.reset_job_ids()  # Reset task IDs after deleting
                return True
        return False
    
    def mark_job_complete_by_id(self, task_id):
        job = self.get_job_by_id(task_id)
        if job:
            job.completed = not job.completed
            return True
        return False

    def get_job_by_id(self, job_id):
        for job in self.jobs:
            if job.job_id == job_id:
                return job
        return None

    def reset_job_ids(self):
        for index, job in enumerate(self.jobs):
            job.job_id = index + 1
        self.last_job_id = len(self.jobs)

    def get_jobs(self):
        return self.jobs

