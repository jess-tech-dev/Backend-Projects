import tkinter as tk
from tkinter import messagebox

# Initialize the application
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

tasks = []

# Functions
def add_task():
    task_name = task_entry.get().strip()
    if task_name:
        tasks.append({"name": task_name, "done": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task name cannot be empty!")

def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def mark_task_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks[task_index]['done'] = True
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✗"
        task_listbox.insert(tk.END, f"{task['name']} [{status}]")

# GUI Layout
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10, padx=20, fill=tk.X)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white", font=("Arial", 12))
add_button.pack(pady=5, padx=20, fill=tk.X)

task_listbox = tk.Listbox(root, font=("Arial", 12), height=15)
task_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

mark_done_button = tk.Button(root, text="Mark as Done", command=mark_task_done, bg="blue", fg="white", font=("Arial", 12))
mark_done_button.pack(pady=5, padx=20, fill=tk.X)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="red", fg="white", font=("Arial", 12))
remove_button.pack(pady=5, padx=20, fill=tk.X)

# Start the application
root.mainloop()