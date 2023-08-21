import os


def show_menu():
    while True:
        print(
            '1 - Importar senhas\n'
            '2 - Exportar senhas\n'
            '3 - Gerar senhas\n'
            '4 - Sair\n'
        )

        option = input('Digite o número correspondente à opção desejada: ')

        if option[0] in '1234':
            break

        os.system('cls')
        print(
            f'[{option}] não é uma opção válida. Por favor, digite uma das opções listadas.')
    return option


def import_menu(func_import=None, func_valid_path=None):

    os.system('cls')

    while True:
        print(
            '1 - Usar diretório padrão (mesma pasta do arquivo que está sendo executado)\n'
            '2 - Escolher diretório e nome do arquivo\n'
        )

        option = input('Digite o número correspondente à opção desejada: ')

        if option[0] in '12':
            os.system('cls')
            break

        os.system('cls')

        print(
            f'[{option}] não é uma opção válida. Por favor, digite uma das opções listadas.')

    match option:

        case '1':

            existing_passwords = func_import()
            filename = 'passwords.txt'

        case '2':

            filepath = input('Digite o caminho da pasta do arquivo que você quer importar.\n'
                             'Por exemplo, se quisesemos buscar um arquivo na pasta "passwords"\n'
                             'obs: para mac e linux, use barras normais. Para windows, 2 barras invertidas.\n'
                             'C:\\Users\\jonat\OneDrive\\Área de Trabalho\\Py\\Random-Password-Generator\\passwords\n\n'
                             'caminho: ')

            os.system('cls')
            print(f'Caminho da pasta: {filepath}\n')

            filename = input('Agora digite o nome do arquivo .txt que você quer importar: \n'
                             'ex: passwords.txt\n\n'
                             'Nome do arquivo: ')

            absolutely_filepath = f'{filepath}\{filename}'

            valid_path = func_valid_path(absolutely_filepath)

            if valid_path:
                os.system('cls')
                existing_passwords = func_import(
                    filename=filename, filepath=filepath)

            else:
                os.system('cls')
                print(
                    f'O caminho "{absolutely_filepath}" não é válido ou não existe.\n')
                existing_passwords = None
            # try:
            #     existing_passwords = func_import(
            #         filename=filename, filepath=filepath)
            # except TypeError:
            #     existing_passwords = set()
    return existing_passwords, filename


def export_menu(func_exportxt, func_valid_path, passwords):

    if passwords is None:
        print('Você ainda não tem senhas para importar! Primeiro gere novas senhas.')
    else:

        while True:

            os.system('cls')
            print(
                '1 - Usar diretório padrão (mesma pasta do arquivo que está sendo executado)\n'
                '2 - Escolher diretório e nome do arquivo\n'
            )

            option = input('Digite o número correspondente à opção desejada: ')

            if option[0] in '12':
                os.system('cls')
                break

            os.system('cls')

            print(
                f'[{option}] não é uma opção válida. Por favor, digite uma das opções listadas.')

        match option:

            case '1':

                func_exportxt(passwords)

            case '2':

                filepath = input('Digite o caminho da pasta para exportar o arquivo: \n'
                                 'Por exemplo, se quisesemos buscar um arquivo na pasta "passwords"\n'
                                 'obs: para mac e linux, use barras normais. Para windows, 2 barras invertidas.'
                                 'C:\\Users\\jonat\OneDrive\\Área de Trabalho\\Py\\Random-Password-Generator\\passwords\n\n'
                                 'caminho:')

                filename = input('Agora digite o nome do arquivo .txt que você quer exportar: \n'
                                 'ex: passwords.txt\n\n'
                                 'Nome do arquivo:')

                absolutely_filepath = f'{filepath}\{filename}'

                valid_path = func_valid_path(absolutely_filepath)

                if valid_path:
                    func_exportxt(passwods=passwords,
                                  filename=filepath, filepath=filepath)

                else:
                    os.system('cls')
                    print(
                        f'O caminho "{absolutely_filepath}" não é válido ou não existe.\n')


def menu_passgen(func_passgen):

    os.system('cls')

    while True:

        print('1 - Gerar senha com padrões do sistema\n'
              '2 - Gerar senha a partir das minhas definições')

        option = input('Digite uma das opções listadas: ')

        if option[0] in '12':
            os.system('cls')
            break

        os.system('cls')
        print('Digite apenas uma das opções listadas.')

    match option:

        case '1':
            generated_passwords = func_passgen()

        case '2':

            while True:
                try:
                    length = int(
                        input('Insire o número de caracteres que a senha deve ter: '))
                    if length >= 2:
                        break
                    os.system('cls')
                    print('O número de caracteres deve ser pelo menos 3.')
                except ValueError:
                    os.system('cls')
                    print('Digite apenas números inteiros!')

            os.system('cls')

            while True:
                try:
                    quantity = int(
                        input('Digite quantas senhas você deseja gerar: '))
                    if quantity > 0:
                        break
                    os.system('cls')
                    print('A quantidade de senhas geradas deve ser pelo menos 1.')
                except ValueError:
                    os.system('cls')
                    print('Digite apenas números inteiros!')

            os.system('cls')

            while True:

                try:
                    numbers = input(
                        'Você deseja incluir números na sua senha? [S]im [N]ão: ').upper()
                    if numbers[0] == 'S':
                        numbers = True
                        break
                    elif numbers[0] == 'N':
                        numbers = False
                        break
                    else:
                        os.system('cls')
                        print('Digite apenas sim ou não!')
                except IndexError:
                    os.system('cls')
                    print('Você não digitou nada :(')

            os.system('cls')

            while True:
                try:
                    lower_case = input(
                        'Você deseja incluir letras minúsculas? na sua senha? [S]im [N]ão: ').upper()
                    if lower_case[0] == 'S':
                        lower_case = True
                        break
                    elif lower_case[0] == 'N':
                        lower_case = False
                        break
                    else:
                        os.system('cls')
                        print('Digite apenas sim ou não!')
                except IndexError:
                    os.system('cls')
                    print('Você não digitou nada :(')

            os.system('cls')

            while True:
                try:
                    upper_case = input(
                        'Você deseja incluir letras maiúsculas? na sua senha? [S]im [N]ão: ').upper()
                    if upper_case[0] == 'S':
                        upper_case = True
                        break
                    elif upper_case[0] == 'N':
                        upper_case = False
                        break
                    else:
                        os.system('cls')
                        print('Digite apenas sim ou não!')
                except IndexError:
                    os.system('cls')
                    print('Você não digitou nada :(')

            os.system('cls')

            while True:

                try:
                    spec_characters = input(
                        'Você deseja incluir caracteres especiais na sua senha? [S]im [N]ão: ').upper()
                    if spec_characters[0] == 'S':
                        spec_characters = True
                        break
                    elif spec_characters[0] == 'N':
                        spec_characters = False
                        break
                    else:
                        os.system('cls')
                        print('Digite apenas sim ou não!')
                except IndexError:
                    os.system('cls')
                    print('Você não digitou nada :(')

            os.system('cls')

            while True:
                try:
                    repeat = input(
                        'Você deseja que os caracteres possam ser repetidos? [S]im [N]ão: ').upper()
                    if repeat[0] == 'S':
                        repeat = True
                        break
                    elif repeat[0] == 'N':
                        repeat = False
                        break
                    else:
                        os.system('cls')
                        print('Digite apenas sim ou não!')
                except IndexError:
                    os.system('cls')
                    print('Você não digitou nada :(')

            os.system('cls')

            generated_passwords = func_passgen(length=length, quantity=quantity, numbers=numbers,
                                               alphabet_lower=lower_case, alphabet_upper=upper_case, special_characters=spec_characters, repeat=repeat)
    os.system('cls')
    print('Senhas geradas!')
    return generated_passwords
