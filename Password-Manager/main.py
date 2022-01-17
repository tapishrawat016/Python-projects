from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops!", message="Please make sure you haven't left any fields empty")


    else:

        try:

            with open("data.json", "r") as data_file:

                # Reading old data

                data = json.load(data_file)

        except FileNotFoundError:

            with open("data.json", "w") as data_file:

                json.dump(new_data, data_file, indent=4)

        else:

            # Updating old data with new data

            data.update(new_data)

            with open("data.json", "w") as data_file:

                # Saving updated data

                json.dump(data, data_file, indent=4)

        finally:

            website_input.delete(0, END)

            password_input.delete(0, END)


# ---------------------------- Search ------------------------------- #
def find_password():
    website_name = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No Data File Found")

    else:
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\n Password: {password}")

        else:
            messagebox.showinfo(title="error", message=f"No details for {website_name} exists. ")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# canvas
my_canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=lock_img)
my_canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Button
generate_pswrd_button = Button(text="Generate Password", command=generate_password)
generate_pswrd_button.grid(row=3, column=2)
add_pswrd_button = Button(text="Add", width=36, command=add_password)
add_pswrd_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

# entry
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1, )
email_input = Entry(width=35)
email_input.insert(0, "tapish@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

window.mainloop()
