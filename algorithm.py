import os.path
import customtkinter as ctk
import random
import string
import tkinter as tk
from tkinter import messagebox
from PIL import Image
from customtkinter import CTkLabel

sLetters = string.ascii_lowercase
cLetters = string.ascii_uppercase
digit = string.digits

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.geometry("600x400")
        master.title("Random Password Generator")

        self.image_path = os.path.join(os.path.dirname(__file__), "images/logo.jpg")
        self.image = ctk.CTkImage(light_image= Image.open(self.image_path),size=(150,50))
        self.image_label = CTkLabel(master=master, image=self.image,text='')
        self.image_label.place(x =430 , y=20)

        self.image1_path = os.path.join(os.path.dirname(__file__), "images/xlogo.png")
        self.image1 = ctk.CTkImage(light_image=Image.open(self.image1_path), size=(20, 20))
        self.image1_label = CTkLabel(master=master, image=self.image1, text='')
        self.image1_label.pack(side='bottom')
        self.image1_label.place(x=255, y=370)

        self.label_image = ctk.CTkLabel(master, text=" @msecurity0")
        self.label_image.place(x =280 , y=370)

        self.label_image = ctk.CTkLabel(master, text_color='gold', text="This project Has been made by: Mansour Albader")
        self.label_image.place(x =170 , y=320)

        self.label_StNum= ctk.CTkLabel(master,text_color='green', text="Student Number: 221110092")
        self.label_StNum.place(x=230, y=340)

        self.entry_length = ctk.CTkEntry(master,placeholder_text='Enter length of password (6-60)',width=200)
        self.entry_length.pack(pady=10)

        self.label_options = ctk.CTkLabel(master, text="Choose at least 1 options:  ")
        self.label_options.pack(pady=5,padx=5)

        self.lowercase_var = tk.BooleanVar()
        self.uppercase_var = tk.BooleanVar()
        self.lowercase_checkbox = ctk.CTkCheckBox(master,corner_radius=10, text="Lowercase [abcd]         ", variable=self.lowercase_var)
        self.uppercase_checkbox = ctk.CTkCheckBox(master,corner_radius=10, text="Uppercase [ABCD]         ", variable=self.uppercase_var)
        self.lowercase_checkbox.pack(pady=5)
        self.uppercase_checkbox.pack(pady=5)

        self.include_numbers_var = tk.BooleanVar()
        self.include_numbers_checkbox = ctk.CTkCheckBox(master, corner_radius=10,text="Include numbers [1234]", variable=self.include_numbers_var)
        self.include_numbers_checkbox.pack(pady=5)

        self.include_symbols_var = tk.BooleanVar()
        self.include_symbols_checkbox = ctk.CTkCheckBox(master,corner_radius=10, text="Include symbols [@#$!]", variable=self.include_symbols_var)
        self.include_symbols_checkbox.pack(pady=5)



        self.entry_quantity = ctk.CTkEntry(master,placeholder_text='Enter length of password (1-100)',width=200)
        self.entry_quantity.pack(pady=5)

        self.generate_button = ctk.CTkButton(master,corner_radius=32, width=400,height=40,text="Generate Password(s)", command=self.generate_passwords)

        self.generate_button.pack(pady=12)

    def generate_passwords(self):
        length = int(self.entry_length.get())
        include_lowercase = self.lowercase_var.get()
        include_uppercase = self.uppercase_var.get()
        include_numbers = self.include_numbers_var.get()
        include_symbols = self.include_symbols_var.get()
        quantity = int(self.entry_quantity.get())


        characters = ''
        if include_lowercase:
            characters += sLetters
        if include_uppercase:
            characters += cLetters
        if include_numbers:
            characters += digit
        if include_symbols:
            characters += string.punctuation

        passwords = []
        if 1 <= quantity <= 100:
            for _ in range(quantity):
                if 6 <= length <= 60:
                    password = ''.join(random.choice(characters) for _ in range(length))
                    passwords.append(password)
                else:
                    s = "password length must be between 6 and 60"
                    passwords.append(s)
        else:
            s = "quantity length must be between 1 and 100"
            passwords.append(s)

        password_str = "\n".join(passwords)
        messagebox.showinfo("Generated Passwords", password_str)
