import passgen

existing_passwords = set(passgen.passimporttxt(
    filename='C:\\Users\\jonat\\OneDrive\\Área de Trabalho\\Py\Random-Password-Generator\\passwords\\Minhas Senhas.txt'))
generated_passwords = passgen.password_gen(length=8, quantity=5, repeat=False)
passgen.passexporttxt(
    generated_passwords, filename='C:\\Users\\jonat\\OneDrive\\Área de Trabalho\\Py\Random-Password-Generator\\passwords\\Minhas senhas.txt')
