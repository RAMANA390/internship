import tkinter as tk
from tkinter import messagebox
import os

# ---------- Save File Name ----------
TASK_FILE = "tasks.txt"

# ---------- Load Tasks from File ----------
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())

# ---------- Save Tasks to File ----------
def save_tasks():
    with open(TASK_FILE, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# ---------- Add Task ----------
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# ---------- Remove Task ----------
def remove_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# ---------- Mark Task as Complete ----------
def mark_done():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        if not task.endswith(" ✔"):
            task += " ✔"
            task_listbox.delete(selected)
            task_listbox.insert(selected, task)
            save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 18))
title_label.pack(pady=10)

# Entry Field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=12)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, width=12)
remove_button.grid(row=0, column=1, padx=5)

done_button = tk.Button(button_frame, text="Mark as Complete", command=mark_done, width=15)
done_button.grid(row=0, column=2, padx=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=10, selectbackground="lightblue")
task_listbox.pack(pady=10)

# Load existing tasks
load_tasks()

# Run App
root.mainloop()
