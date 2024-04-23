import tkinter as tk
from tkinter import messagebox

def register():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    print("New Username:", new_username)
    print("New Password:", new_password)
    messagebox.showinfo("Registration Successful", "Registration successful for {}".format(new_username))

    register_window.withdraw()
    login_window.deiconify()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == new_username_entry.get() and password == new_password_entry.get():
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

register_window = tk.Tk()
register_window.title("Register")

new_username_label = tk.Label(register_window, text="New Username:")
new_username_label.grid(row=0, column=0, padx=10, pady=5)
new_username_entry = tk.Entry(register_window)
new_username_entry.grid(row=0, column=1, padx=10, pady=5)

new_password_label = tk.Label(register_window, text="New Password:")
new_password_label.grid(row=1, column=0, padx=10, pady=5)
new_password_entry = tk.Entry(register_window, show="*")
new_password_entry.grid(row=1, column=1, padx=10, pady=5)

register_button = tk.Button(register_window, text="Register", command=register)
register_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

login_window = tk.Tk()
login_window.title("Login")
login_window.withdraw()

username_label = tk.Label(login_window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(login_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(login_window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

register_window.mainloop()