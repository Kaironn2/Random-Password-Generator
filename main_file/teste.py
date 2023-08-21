from passgen import password_gen
from importexport import passexporttxt, passimporttxt
from menu import show_menu, import_menu
import os

while True:

    option = show_menu()

    match option:

        case '1':

            existing_passwords = import_menu(passimporttxt)


generated_passwords = password_gen(length=8, quantity=6, repeat=False)

passexporttxt(generated_passwords, filename='TESTES')
