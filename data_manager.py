from job import Job


class DataManager:
    def __init__(self, file_path="jobs.txt"):
        self.file_path = file_path

    # Reads the jobs from the jobs.txt file
    def load_jobs(self):
        jobs = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    job_data = line.strip().split(",")
                    job_id = int(job_data[0])
                    name = job_data[1]
                    job_completed = job_data[2] == 'True'
                    job = Job(job_id, name, job_completed)
                    jobs.append(job)
        except FileNotFoundError:
            print("No data file found. Returning an empty task list.")
        return jobs

    # Saves the jobs the user input to jobs.txt
    def save_jobs(self, jobs):
        try:
            with open(self.file_path, "w") as file:
                for job in jobs:
                    job_data = [str(job.job_id), job.name, str(job.completed)]
                    file.write(",".join(job_data) + "\n")
        except IOError:
            print("An error occurred while saving the tasks.")

