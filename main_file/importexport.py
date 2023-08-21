import os


def passexporttxt(passwords, filename=None, filepath=None):
    if filename is None:
        filename = 'passwords.txt'

    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__))

    absolutely_filepath = f'{filepath}\{filename}'

    with open(absolutely_filepath, 'a') as file:
        for password in passwords:
            file.write(password + '\n')
        print(f'Senhas exportadas para o arquivo: {filename}\n'
              f'Caminho do arquivo: {absolutely_filepath}')


def passimporttxt(filename=None, filepath=None):
    if filename is None:
        filename = 'passwords.txt'

    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__))

    try:
        with open(filename, 'r') as file:
            passwords = [line.strip() for line in file]

        return passwords
    except FileNotFoundError:
        print('Arquivo não existe para importar.')
