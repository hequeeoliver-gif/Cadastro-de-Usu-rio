import re

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)  

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"


nome = input("escreva seu nome por favor ")
while nome == "":
    nome = input("nome vazio não é valido escreva de novo por favor ")

email = input("escreva seu email por favor ")
while not "@" in email or not "." in email:
    email = input("email invalido escreva de novo por favor ")

cpf = input("digite seu cpf ")
while not validar_cpf(cpf):
    cpf = input("CPF inválido. Digite novamente por favor ")

print("\nDados válidos:")
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"CPF: {cpf}")

