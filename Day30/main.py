from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
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
    new_data = {
        website_info: {
            "email": e_mail_info,
            "password": password_info,
        }
    }
    
    
    if len(website_info) == 0 or len(e_mail_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                e_mail_entry.delete(0, END)
                
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"E-mail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
        
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
website_entry = Entry(width=22, font=("Left"))
website_entry.grid(column=1, row=1)
website_entry.focus()
e_mail_entry = Entry(width=34, font=("Left"))
e_mail_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=22, font=("Left"))
password_entry.grid(column=1, row=3)

#Buttons
search_button = Button(width=17, text="Search", command=find_password)
search_button.grid(column=2, row=1)
genreate_button = Button(width=17, text="Generate Password", command=password_generator)
genreate_button.grid(column=2, row=3)
add_button = Button(width=34, text="Add", font=("Left"), command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()