from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]  #random letters for password
    [password_list.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]   #random symbols for password
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]   #random numbers for password

    random.shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_user_text.get()
    password = password_text.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        with open("data.json", "r") as data_file:  #In this format it read, updates, and adds new
            data = json.load(data_file)
            data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

            website_text.delete(0, END)
            password_text.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_user = Label(text="Email/Username:")
email_user.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

#text entry
website_text = Entry(width=38)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

email_user_text = Entry(width=38)
email_user_text.grid(row=2, column=1, columnspan=2)

password_text = Entry(width=21)
password_text.grid(row=3, column=1)

#Buttons
generate = Button(text="Generate password", command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)



window.mainloop()