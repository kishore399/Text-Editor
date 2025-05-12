import tkinter as tk
from tkinter import ttk, messagebox

# Main window
root = tk.Tk()
root.title("Notepad")
root.geometry("500x500")

# Notebook ->
notebook = ttk.Notebook(root, style="TNotebook")
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Adds notes ->
def add():
    # new tab ->
    frame = ttk.Frame(notebook, padding=10)
    notebook.add(frame, text="New_note")
    
    # inputs ->
    tl = ttk.Label(frame, text="Title:")
    tl.grid(row=0, column=0, padx=10, pady=10, sticky="W")
    ti = ttk.Entry(frame, width=40)
    ti.grid(row=0, column=1, padx=10, pady=10)

    cl = ttk.Label(frame, text="Content:")
    cl.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    ci = tk.Text(frame, width=40, height=10)
    ci.grid(row=1, column=1, padx=10, pady=10)
    
    # Save function ->
    def save():
        # Getting input
        title = ti.get()
        content = ci.get("1.0", tk.END)

        # if title is empty ->
        if title.strip() == "":
            messagebox.showwarning("Title Required", "Please enter a title!")
            return

        #Saving input
        ncontent = tk.Text(notebook, width=40, height=10)
        ncontent.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(ncontent, text=title)
        
    # Save button ->
    sbtn = ttk.Button(frame, text="Save", command=save, style="secondary.TButton")
    sbtn.grid(row=2, column=1, padx=10, pady=10)


# Deletes Notes ->
def delete():
    # Current tab
    curr = notebook.index(notebook.select())
    del_title = notebook.tab(curr, "text")

    d = messagebox.askquestion("Delete", f"Do you really want to delete {del_title}?")
    if d == "yes":
        notebook.forget(curr)

# new note - button ->
nbtn = ttk.Button(root, text="New Note", command=add)
nbtn.pack(side=tk.LEFT, padx=10, pady=10)

# Delete note - button ->
dbtn = ttk.Button(root, text="Delete", command=delete)
dbtn.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()