# A simple TO-DO List Manager

import tkinter as tk
from tkinter import messagebox, filedialog

# Initialize the Tkinter window
root = tk.Tk()
root.title("To-Do List Manager")

# Initialize the to-do list
todo_list = []

# Define functions for actions
def view_list():
    listbox.delete(0, tk.END)
    for i, item in enumerate(todo_list):
        listbox.insert(tk.END, f"{i+1}. {item}")

def add_item():
    item = entry.get()
    if item:
        if item in todo_list:
            messagebox.showerror("Error", f"'{item}' already exists in your to-do list.")
        else:
            todo_list.append(item)
            view_list()
            entry.delete(0, tk.END)

def remove_item():
    try:
        index = int(listbox.curselection()[0])
        item_to_remove = todo_list.pop(index)
        messagebox.showinfo("Success", f"Removed '{item_to_remove}' from your to-do list.")
        view_list()
    except IndexError:
        messagebox.showerror("Error", "Please select an item to remove.")

def erase_list():
    if messagebox.askyesno("Confirmation", "Are you sure you want to erase the entire to-do list? This action cannot be undone."):
        todo_list.clear()
        view_list()

def save_list():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, "w") as f:
            for item in todo_list:
                f.write(item + "\n")
        messagebox.showinfo("Success", "To-do list saved successfully.")

def load_list():
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        try:
            with open(filename, "r") as f:
                for line in f:
                    todo_list.append(line.strip())
            view_list()
        except FileNotFoundError:
            pass

def handle_keyboard(event):
    if event.keysym == 'Return' and event.state == 4:  # Ctrl + Enter
        add_item()
    elif event.keysym == 'Delete':
        remove_item()
    elif event.keysym == 'E' and event.state == 12:  # Ctrl + Shift + E
        erase_list()

def handle_enter(event):
    if event.keysym == 'Return':
        add_item()

# Create GUI elements
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter new item:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

add_button = tk.Button(frame, text="Add", command=add_item)
add_button.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.grid(row=1, columnspan=3, pady=10)

remove_button = tk.Button(frame, text="Remove", command=remove_item)
remove_button.grid(row=2, column=0, pady=5)

erase_button = tk.Button(frame, text="Erase List", command=erase_list)
erase_button.grid(row=2, column=2, pady=5)

save_button = tk.Button(frame, text="Save", command=save_list)
save_button.grid(row=3, column=0, pady=5)

load_button = tk.Button(frame, text="Load", command=load_list)
load_button.grid(row=3, column=2, pady=5)

# Bind keyboard events
root.bind("<KeyPress>", handle_keyboard)
entry.bind("<KeyPress>", handle_enter)

# Customize appearance
root.configure(bg='#f0f0f0')
frame.configure(bg='#f0f0f0')
label.configure(bg='#f0f0f0', fg='#333333', font=('Arial', 12))
entry.configure(bg='white', fg='#333333', font=('Arial', 12))
add_button.configure(bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
listbox.configure(bg='white', fg='#333333', font=('Arial', 12))
remove_button.configure(bg='#FF5722', fg='white', font=('Arial', 12, 'bold'))
erase_button.configure(bg='#F44336', fg='white', font=('Arial', 12, 'bold'))
save_button.configure(bg='#2196F3', fg='white', font=('Arial', 12, 'bold'))
load_button.configure(bg='#2196F3', fg='white', font=('Arial', 12, 'bold'))

# Run the Tkinter event loop
root.mainloop()
