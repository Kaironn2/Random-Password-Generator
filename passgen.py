import string
import random
import os


def password_gen(
        length=8, quantity=1, numbers=True, alphabet_lower=True,
        alphabet_upper=True, special_characters=True, repeat=True, existing_passwords=None):

    characters = ''
    spec_characters = '!@#$%&*'
    passwords = []

    if numbers:
        characters += string.digits

    if alphabet_lower:
        characters += string.ascii_lowercase

    if alphabet_upper:
        characters += string.ascii_uppercase

    if special_characters:
        characters += spec_characters

    if not characters:
        raise ValueError(
            'Nenhum conjunto de caracteres selecionado. Pelo menos um dos conjuntos tem que ser True')

    if existing_passwords is None:
        existing_passwords = set()

    for _ in range(quantity):
        while True:
            if repeat:
                password = ''.join(random.choice(characters)
                                   for _ in range(length))
            else:
                if length > len(characters):
                    raise ValueError(
                        f'A quantidade de caracteres definidos para a senha é maior que o número de caracteres disponíveis, sendo o máximo {len(characters)} caracteres.')

                password = ''.join(random.sample(characters, length))

            if password not in existing_passwords:
                existing_passwords.add(password)
                passwords.append(password)
                break

    return passwords


def passexporttxt(passwords, filename=None):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), 'passwords.txt')

    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')
        print('Senhas exportadas!')


def passimporttxt(filename=None):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), 'passwords.txt')

    try:
        with open(filename, 'r') as file:
            passwords = [line.strip() for line in file]

        return passwords
    except FileNotFoundError:
        print('Arquivo não existe para importar.')
