from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops!", message="Please make sure you haven't left any fields empty")

    else:

        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered:\nEmail :{email} "
                                                           f"\n Password :{password}\n Is is ok to save? ")
        if is_ok:
            with open("password_manager.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


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
generate_pswrd_button = Button(text="Generate Password",command=generate_password)
generate_pswrd_button.grid(row=3, column=2)
add_pswrd_button = Button(text="Add", width=36, command=add_password)
add_pswrd_button.grid(row=4, column=1, columnspan=2)

# entry
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)
email_input = Entry(width=35)
email_input.insert(0, "tapish@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

window.mainloop()
