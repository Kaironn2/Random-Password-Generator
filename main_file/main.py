from passgen import password_gen
from importxt import importxt, show_imported_passwords, existing_passwords, imported_filename
from exportxt import exporttxt, is_valid_path
from menu import show_menu, import_menu, export_menu, menu_passgen
from passgen import password_gen
import os

generated_passwords = None

while True:

    show_imported_passwords(existing_passwords, imported_filename)

    option = show_menu()

    match option:

        case '1':

            os.system('cls')
            existing_passwords, imported_filename = import_menu(
                func_import=importxt, func_valid_path=is_valid_path)

        case '2':

            os.system('cls')
            export_menu(func_exportxt=exporttxt,
                        func_valid_path=is_valid_path, passwords=generated_passwords)

        case '3':

            generated_passwords = menu_passgen(password_gen)

        case '4':

            break
