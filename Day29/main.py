from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_info = website_entry.get()
    e_mail_info = e_mail_entry.get()
    password_info = password_entry.get()
    
    if len(website_info) == 0 or len(e_mail_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_info, message=f"These are the details entered: \nEmail: {e_mail_info} \nPassword: {password_info} \nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_info} | {e_mail_info} | {password_info}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                e_mail_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
e_mail = Label(text="E-mail/Username:")
e_mail.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
 
#Entries
website_entry = Entry(width=34, font=("Left"))
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
e_mail_entry = Entry(width=34, font=("Left"))
e_mail_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21, font=("Left"))
password_entry.grid(column=1, row=3)

#Buttons
genreate_button = Button(text="Generate Password", command=password_generator)
genreate_button.grid(column=2, row=3)
add_button = Button(width=34, text="Add", font=("Left"), command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()