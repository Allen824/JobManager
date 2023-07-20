import tkinter as tk
from tkinter import messagebox
from job import Job


class ToDoListGUI(tk.Frame):
    def __init__(self, master, job_manager, data_manager):
        super().__init__(master)
        self.master = master
        self.job_manager = job_manager
        self.data_manager = data_manager

        self.master.title("Job List")
        self.master.geometry("500x500")

        self.job_entries = []

        self.create_widgets()
        self.populate_job_list()
        self.highlight_completed_jobs()

    # Tkinter widgets that will appear in the GUI
    def create_widgets(self):
        self.job_frame = tk.Frame(self.master)
        self.job_frame.pack(pady=10)

        # Add job widgets
        self.job_label = tk.Label(self.job_frame, text="Job:")
        self.job_label.grid(row=0, column=0, padx=5)

        self.job_entry = tk.Entry(self.job_frame, width=30)
        self.job_entry.grid(row=0, column=1, padx=5)

        self.add_button = tk.Button(self.master, text="Add Job", command=self.add_job)
        self.add_button.pack(pady=5)

        # Widget for displaying jobs
        self.job_listbox = tk.Listbox(self.master, width=40)
        self.job_listbox.pack(pady=10)

        # Mark complete widget
        self.complete_button = tk.Button(self.master, text="Mark Complete", command=self.mark_job_complete)
        self.complete_button.pack(pady=5)

        # Delete job widget
        self.delete_button = tk.Button(self.master, text="Delete Job", command=self.delete_job)
        self.delete_button.pack(pady=5)

        # Search widgets
        self.job_frame = tk.Frame(self.master)
        self.job_frame.pack(pady=10)

        self.search_label = tk.Label(self.job_frame, text="Search:")
        self.search_label.grid(row=0, column=0, padx=5)

        self.search_entry = tk.Entry(self.job_frame, width=30)
        self.search_entry.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.master, text="Search", command=self.search_jobs)
        self.delete_button.pack(pady=5)



    # Populates job list with jobs
    def populate_job_list(self, jobs=None):
        self.job_listbox.delete(0, tk.END)
        jobs = jobs or self.job_manager.get_jobs()
        for job in jobs:
            job_info = f"{job.job_id}: {job.name}"
            self.job_listbox.insert(tk.END, job_info)
            

    # Method for adding a job to a list
    def add_job(self):
        job_name = self.job_entry.get().strip()
        if job_name:
            job_id = len(self.job_manager.get_jobs()) + 1
            job = Job(job_id, job_name, False)
            self.job_manager.add_job(job)
            self.job_entry.delete(0, tk.END)
            self.populate_job_list()
            self.highlight_completed_jobs()
            self.data_manager.save_jobs(self.job_manager.get_jobs())
        else:
            messagebox.showwarning("No Job", "Please enter a job name.")

    # Method for marking a job complete
    def mark_job_complete(self):
        job_id = self.get_selected_job_id()
        if job_id is not None:
            if self.job_manager.mark_job_complete_by_id(job_id):
                self.populate_job_list()
                self.data_manager.save_jobs(self.job_manager.get_jobs())
                self.highlight_completed_jobs()
            else:
                messagebox.showwarning("Job Not Found", "The selected job ID does not exist.")
        else:
            messagebox.showwarning("No Job Selected", "Please select a job to mark as complete.")

    # Gets the id of current selection
    def get_selected_job_id(self):
        selected_index = self.job_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            job_info = self.job_listbox.get(index)
            job_id = int(job_info.split(":")[0])
            return job_id
        return None
    
    # Highlights a job to show its completed
    def highlight_completed_jobs(self):
        for index in range(self.job_listbox.size()):
            job_info = self.job_listbox.get(index)
            job_id = int(job_info.split(":")[0])
            job_completed = self.job_manager.get_job_by_id(job_id).completed
            if job_completed:
                self.job_listbox.itemconfig(index, {'bg': 'lightgreen'})
            # unhighlights job if "marked completed" button is triggered again
            else:
                self.job_listbox.itemconfig(index, {'bg': 'white'})

    # Method for deleting a job from a list
    def delete_job(self):
        selected_index = self.job_listbox.curselection() 
        
        if selected_index:
                index = selected_index
                job_info = self.job_listbox.get(index)
                job_id = int(job_info.split(":")[0])
                if self.job_manager.delete_job_by_id(job_id):
                    self.populate_job_list()
                    self.highlight_completed_jobs()
                    self.data_manager.save_jobs(self.job_manager.get_jobs())
                else:
                    messagebox.showwarning("Job Not Found", "The selected job ID does not exist.")
        else:
            messagebox.showwarning("No job Selected", "Please select a job to delete.")

    # Method for search functionality
    def search_jobs(self):
        search_name = self.search_entry.get().lower()
        jobs = self.job_manager.get_jobs()
        if search_name:
            jobs = self.job_manager.get_jobs()
            found_jobs = [job for job in jobs if search_name in job.name.lower()]


            if found_jobs == []: 
                messagebox.showwarning("Not Found", "No matching results were found.")
            else:   
                # Widgets for the results window after the user searches
                result_window = tk.Toplevel(self.master)
                result_window.title("Search Results")

                self.result_listbox = tk.Listbox(result_window, width=40)
                self.result_listbox.pack()

                self.result_listbox.delete(0, tk.END)
                for job in found_jobs:
                    self.result_listbox.insert(tk.END, f"{job.job_id}: {job.name}")

        else:
            messagebox.showwarning("Search Empty", "Enter the job you want to search for.")







