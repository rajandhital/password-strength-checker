import tkinter as tk
from tkinter import messagebox
import re

# List of weak/common passwords
weak_passwords = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "12345678", "iloveyou", "admin", "letmein"
]

# Function to evaluate password strength
def evaluate_password():
    password = entry.get()
    suggestions = []

    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    # Rules
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Include at least one lowercase letter.")
    if not re.search(r"\d", password):
        suggestions.append("Include at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Include at least one special character.")
    if password.lower() in weak_passwords:
        suggestions.append("Avoid using common passwords.")

    # Determine score
    score = 5 - len(suggestions)
    status = "Strong" if score == 5 else "Weak"

    # Build result message
    result_message = f"Password Strength: {status} ({score}/5)"
    if suggestions:
        result_message += "\nSuggestions:\n" + "\n".join(suggestions)

    if score < 4:
        messagebox.showwarning("Weak Password", result_message)
    else:
        messagebox.showinfo("Password Strength", result_message)

# Toggle password visibility
def toggle_password():
    if show_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

# Checkbox for show/hide password
show_var = tk.BooleanVar()
show_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password)
show_checkbox.pack(pady=5)

button = tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 12), bg="blue", fg="white")
button.pack(pady=20)

root.mainloop()
