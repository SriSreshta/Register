import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if not name or not email or not phone:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return
    
    # Here you can add code to process the registration, e.g., save to a file or database
    # For this example, we'll just show a success message
    messagebox.showinfo("Registration Successful", f"Thank you for registering, {name}!")

# Create the main window
root = tk.Tk()
root.title("Event Registration Form")

# Create and place labels and entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Phone:").grid(row=2, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Register", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
