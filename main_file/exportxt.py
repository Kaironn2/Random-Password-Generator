import os


def exporttxt(passwords, filename=None, filepath=None):
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


def is_valid_path(path):
    return os.path.exists(path)

