from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [chr(i).lower() for i in range(65, 91)]
    numbers = [i for i in range(0, 10)]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [str(random.choice(letters)) for _ in range(nr_letters)]
    password_symbols = [str(random.choice(symbols)) for _ in range(nr_symbols)]
    password_numbers = [str(random.choice(numbers)) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        accept = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n Password: {password}\n Is it ok to save?")

        if accept:
            with open("data.txt", "a+") as file:
                file.write(f"{website} | {email} |  {password} \n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


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


gen_btn = Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
add_btn = Button(text="Add", width=36, command=save).grid(row=4, column=1, columnspan=2)

mainloop()