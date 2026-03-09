# Create a graphical to-do list with `tkinter`. This good Python project introduces GUI programming and event-driven design.

import tkinter as tk

fPath = "ToDoList.txt"

# Store checkbox variables and widgets
all_task_vars = []
all_checkboxes = []

# Save tasks to file
def save_tasks():
    #Save all tasks to the file with '- x -' for checked ones.
    with open(fPath, "w") as f:
        for var, cb in zip(all_task_vars, all_checkboxes):
            text = cb.cget("text")
            if var.get():  # checked → add prefix
                f.write(f"- x - {text}\n")
            else:         # unchecked → just base text
                f.write(f"{text}\n")

# Callback when checkbox toggles, to overwrie file for saving
def checkbox_changed(var):
    save_tasks()

# Load tasks from file
def load_tasks():
    try:
        with open(fPath, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    for ln in lines:
        ln = ln.strip()
        checked = False
        text = ln
        if ln.startswith("- x - "):
            checked = True
            text = ln[len("- x - "):]  # strip prefix

        var = tk.BooleanVar(value=checked)
        cb = tk.Checkbutton(frameB, text=text, variable=var)
        cb.pack(anchor="w")

        # Store references
        all_task_vars.append(var)
        all_checkboxes.append(cb)

        # Add listener to toggle
        var.trace_add("write", lambda *args, v=var: checkbox_changed(v))


# Add a new task
def add_task():
    task_text = entry.get().strip()
    if not task_text:
        return
    var = tk.BooleanVar(value=False) # new task is set to false, it's new, not done :)
    cb = tk.Checkbutton(frameB, text=task_text, variable=var)
    cb.pack(anchor="w")
    all_task_vars.append(var)
    all_checkboxes.append(cb)
    var.trace_add("write", lambda *args, v=var: checkbox_changed(v))
    save_tasks()
    entry.delete(0, tk.END)

# delete all tasks
def delete_all_tasks():
    file = open(fPath,"w")
    file.seek(0)
    for i in all_checkboxes:
        i.destroy()
    all_checkboxes.clear()
    all_task_vars.clear()
    file.write("")

def delete_completed_tasks():
    for i in reversed(range(len(all_checkboxes))): # reverse since we're removing items and it can accidently cause us to skip some things
        var = all_task_vars[i]
        cb = all_checkboxes[i]
        if var.get():  # checkbox is checked (value is 1 if checked, 1 is true)
            cb.destroy()            # remove from GUI
            del all_checkboxes[i] # remove widget reference
            del all_task_vars[i]    # remove variable reference
    # Save remaining tasks back to file
    save_tasks()

# GUI setup
window = tk.Tk()
window.title("To-Do List")

frameA = tk.Frame(window)
frameB = tk.Frame(window)
frameTop = tk.Frame(window)

label = tk.Label(window, text="TO DO", fg="white", bg="black", height=2)
label.pack(fill=tk.X)

delAllBtn = tk.Button(frameTop,text="Delete All Tasks", command=delete_all_tasks)
delAllBtn.pack(side=tk.LEFT)

delCompBtn = tk.Button(frameTop,text="Delete All Completed Tasks", command=delete_completed_tasks)
delCompBtn.pack(side=tk.RIGHT)

entry = tk.Entry(frameA)
entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

button = tk.Button(frameA, text="Add Task", command=add_task)
button.pack(side=tk.LEFT)

frameTop.pack(fill=tk.X)
frameA.pack(fill=tk.X)
frameB.pack(fill=tk.BOTH, expand=True)

# Load tasks from file
load_tasks()

window.mainloop()