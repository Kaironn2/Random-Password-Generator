import os

existing_passwords = None
imported_filename = None


def importxt(filename=None, filepath=None):
    if filename is None:
        filename = 'passwords.txt'

    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__))

    absolutely_filepath = f'{filepath}\{filename}'

    try:
        with open(absolutely_filepath, 'r') as file:
            passwords = [line.strip() for line in file]

        return passwords, filename
    except FileNotFoundError:
        print('Arquivo não existe para importar.')


def show_imported_passwords(passwords=None, filename=None):

    if passwords is not None:
        print(f'Senhas importadas! ')
        for password in passwords:
            if password != passwords[-1]:
                print(password, end=' | ')
            else:
                print(password, '\n')
