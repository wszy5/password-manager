# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    with open("data.txt", "a+") as file:
        file.write(f"{website} | {email} |  {password} \n")
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

photo = PhotoImage(file="logo.gif")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_label.config(pady=20)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "wikoszyman@wp.pl")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)


gen_btn = Button(text="Generate Password").grid(row=3, column=2)
add_btn = Button(text="Add", width=36, command=save).grid(row=4, column=1, columnspan=2)

mainloop()