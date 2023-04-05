import random
import string
import tkinter as tk

# Define the GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x300")


def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    password_display.delete(0, tk.END)
    password_display.insert(0, password)

# Add a label for password length
length_label = tk.Label(text="Password Length:")
length_label.pack()

# Add an entry for password length
length_entry = tk.Entry()
length_entry.pack()

# Add a button to generate the password
generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.pack()

# Add a label to display the password
password_label = tk.Label(text="Password:")
password_label.pack()

# Add an entry to display the password
password_display = tk.Entry()
password_display.pack()


window.mainloop()