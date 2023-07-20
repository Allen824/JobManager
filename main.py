import tkinter as tk
from gui import ToDoListGUI
from job_manager import JobManager
from data_manager import DataManager

job_manager = JobManager()
data_manager = DataManager()

# Loads jobs from a file 
jobs = data_manager.load_jobs()

# Jobs are added to the job manager
for job in jobs:
    job_manager.add_job(job)

# Main window 
root = tk.Tk()
app = ToDoListGUI(root, job_manager, data_manager)
app.pack()

# Tkinter event loop
root.mainloop()

data_manager.save_jobs(job_manager.get_jobs())


