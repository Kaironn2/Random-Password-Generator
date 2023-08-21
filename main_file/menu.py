import os


def show_menu():
    while True:
        print(
            '1 - Importar senhas'
            '2 - Exportar senhas'
            '3 - Gerar senhas'
            '4 - Sair'
        )

        option = input('Digite o número correspondente à opção desejada: ')

        if option[0] in '1234':
            break

        os.system('cls')
        print(
            f'[{option}] não é uma opção válida. Por favor, digite uma das opções listadas.')
    return option


def import_menu(func_import):
    
    while True:
        print(
            '1 - Usar diretório padrão (mesma pasta do arquivo que está sendo executado)'
            '2 - Escolher diretório e nome do arquivo'
        )

        option = input('Digite o número correspondente à opção desejada: ')

        if option[0] in '12':
            break

        os.system('cls')

        print(
            f'[{option}] não é uma opção válida. Por favor, digite uma das opções listadas.')

    match option:

        case '1':

            existing_passwords = func_import()

        case '2':
            
            filepath = input('Digite o caminho da pasta do arquivo que você quer importar.\n'
                             'Ex, se o arquivo estiver numa pasta chamada "passwords":\n'
                             'C:\Users\rosan\Desktop\Py\Random-Password-Generator\passwords\n\n'
                             'caminho:')
            
            filename = input('Agora digite o nome do arquivo .txt que você quer importar: \n'
                             'ex: passwords.txt\n\n'
                             'Nome do arquivo:')
            try:
                existing_passwords = func_import(filename=filename, filepath=filepath)
            except TypeError:
                existing_passwords = set()
                
    return existing_passwords