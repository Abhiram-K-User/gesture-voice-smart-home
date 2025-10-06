# ui_login.py
import tkinter as tk
from tkinter import messagebox
from auth import validate_user
from gesture_control import start_gesture_control

def run_login_ui():
    """Tkinter-based login UI for authentication."""
    root = tk.Tk()
    root.title("Smart Home Login")
    root.geometry("300x200")

    tk.Label(root, text="Username:").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def on_login():
        if validate_user(username_entry.get(), password_entry.get()):
            root.destroy()
            start_gesture_control()
        else:
            messagebox.showerror("Authentication Failed", "Invalid username or password.")

    tk.Button(root, text="Login", command=on_login).pack(pady=20)
    root.mainloop()
