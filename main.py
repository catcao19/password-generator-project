from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = randint(8, 10)
nr_numbers = randint(2,4)
nr_symbols = randint(2, 4)
def password_generator():
    password_list = [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any field empty ")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email: {email}\n Password: {password}\n Is it ok to save?")
        if is_ok:
            with open(file="data.txt", mode="a") as f:
                f.write(website + " | " + email + " | " + password + "\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=35)
"""
    End: very last character at the entry (to insert after the text)
    0: insert at the very beginning at the text
    """
email_username_entry.insert(0, "dummy_email@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
