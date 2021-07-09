from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# must be flat, groove, raised, ridge, solid, or sunken
RELIEF = "raised"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(10, 15))]
    password_numbers = [choice(numbers) for _ in range(randint(4, 9))]
    password_symbols = [choice(symbols) for _ in range(randint(4, 9))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_e.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# take website, email and password inputs
# store in "data.txt" file when user clicks add_b


def save():
    website = website_e.get()
    email = email_username_e.get()
    password = password_e.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            # try to open the file if it exists
            with open("./data.json", "r") as data_file:
                # read from json file, json.load(data_file), will convert json contents to a python dict
                data = json.load(data_file)
        except FileNotFoundError:
            # if FielNotFoundError, create a new file (data.json) and write "w"
            with open("./data.json", "w") as data_file:
                # write to json file, json.dump(new_dict name, data_file, indent=4) "w" for open
                # json.dump("what", "where", indent=4)
                json.dump(new_data, data_file, indent=4)
        else:
            # if the file was found, update the data with the new data, only if try ==True
            # update json file, "readable_json file".update(dict_name), "r" for open
            data.update(new_data)

            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_e.delete(0, END)
            password_e.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_e.get()
    try:
        with open("./data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            # to get ahold of email input --> dict["key" the email is in]["value" the email is appended to
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# row 0
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)
# canvas.grid(column=1, row=0)

# row 1
website_l = Label(text="Website:")
website_l.grid(column=0, row=1)

website_e = Entry(width=21)
website_e.focus()
website_e.grid(column=1, row=1)

search_b = Button(text="Search", width=15, bd=1, relief=RELIEF, command=find_password)
search_b.grid(column=2, row=1)

# row 2
email_username_l = Label(text="Email/Username:")
email_username_l.grid(column=0, row=2)

email_username_e = Entry(width=41)
email_username_e.insert(0, "messier.spheroid@gmail.com")
email_username_e.grid(column=1, row=2, columnspan=2)

# row 3
password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

password_e = Entry(width=21)
password_e.grid(column=1, row=3)

generate_password_b = Button(text="Generate Password", width=15, bd=1, relief=RELIEF,
                             command=generate_password)
generate_password_b.grid(column=2, row=3)

# row 4
add_b = Button(text="Add", width=35, bd=1, relief=RELIEF, command=save)
add_b.grid(column=1, row=4, columnspan=2)

window.mainloop()
