import tkinter as tk
from tkinter import messagebox, scrolledtext
import datetime

# Function to get current date & time
def getdate():
    return datetime.datetime.now()

# Function to log data
def take():
    client = client_entry.get().strip().lower()
    action = action_var.get()
    value = entry.get("1.0", tk.END).strip()

    if not client:
        messagebox.showerror("Input Error", "Please enter a client name!")
        return
    
    if action not in ["Exercise", "Food"]:
        messagebox.showerror("Input Error", "Please select an action!")
        return

    if not value:
        messagebox.showerror("Input Error", "Please enter some data!")
        return

    category = "ex" if action == "Exercise" else "food"
    filename = f"{client}-{category}.txt"
    
    with open(filename, "a") as file:
        file.write(f"{getdate()}: {value}\n")
    
    messagebox.showinfo("Success", f"Data logged successfully for {client}!")
    entry.delete("1.0", tk.END)

# Function to retrieve data
def retrieve():
    client = client_entry.get().strip().lower()
    action = action_var.get()

    if not client:
        messagebox.showerror("Input Error", "Please enter a client name!")
        return
    
    if action not in ["Exercise", "Food"]:
        messagebox.showerror("Input Error", "Please select an action!")
        return

    category = "ex" if action == "Exercise" else "food"
    filename = f"{client}-{category}.txt"

    try:
        with open(filename, "r") as file:
            records = file.read()
            text_area.config(state=tk.NORMAL)
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, records)
            text_area.config(state=tk.DISABLED)
    except FileNotFoundError:
        messagebox.showwarning("No Records", f"No records found for {client}!")

# Creating main window
root = tk.Tk()
root.title("Health Management System")
root.geometry("500x500")
root.config(bg="lightblue")

# Title Label
tk.Label(root, text="Health Management System", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

# Client Name Entry
tk.Label(root, text="Enter Client Name:", font=("Arial", 12), bg="lightblue").pack()
client_entry = tk.Entry(root, font=("Arial", 12))
client_entry.pack()

# Action Selection (Dropdown)
tk.Label(root, text="Select Action:", font=("Arial", 12), bg="lightblue").pack()
action_var = tk.StringVar()
action_var.set("Select")  # Default value
action_menu = tk.OptionMenu(root, action_var, "Exercise", "Food")
action_menu.pack()

# Input Text Box
tk.Label(root, text="Enter Details:", font=("Arial", 12), bg="lightblue").pack()
entry = tk.Text(root, height=3, width=40)
entry.pack()

# Buttons
tk.Button(root, text="Log Data", font=("Arial", 12), bg="green", fg="white", command=take).pack(pady=5)
tk.Button(root, text="Retrieve Data", font=("Arial", 12), bg="blue", fg="white", command=retrieve).pack(pady=5)

# Display Area
tk.Label(root, text="Records:", font=("Arial", 12), bg="lightblue").pack()
text_area = scrolledtext.ScrolledText(root, height=10, width=50, state=tk.DISABLED)
text_area.pack()

# Run application
root.mainloop()
