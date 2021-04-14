from tkinter import *
from tkinter import messagebox
import random
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

    password_list = []
    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [password_list.append((random.choice(symbols))) for _ in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # copy to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_var = website_entry.get()
    email_var = email_entry.get()
    password_var = password_entry.get()

    if len(website_var) == 0 or len(password_var) == 0:
        messagebox.showinfo(title="oops", message="you left some field empty.")
    else:
        is_ok = messagebox.askokcancel(title="Check Entry",
                                       message=f"Are entry entered correct?\nWebsite: {website_var}"
                                       f"\nEmail: {email_var} \nPassword: {password_var}")
        if is_ok:
            file = open("data.txt", "a")  # read the text file for appending
            file.write(f"{website_var} | {email_var} | {password_var}\n")  # write to that file
            file.close()
            website_entry.delete(0, END)  # delete all the characters from the widget
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas_img = canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/UserName:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
website_entry = Entry(width=56)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=56)
email_entry.insert(0, "ramin_karimi2003@yahoo.ca")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=56)
password_entry.grid(row=3, column=1, columnspan=2)

password_button = Button(text="Generate Password", font=("Times", 8, "normal"), width=15, command=generate_password)
password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=48, command=add)
add_button.grid(row=4, column=1, columnspan=2)
mainloop()
