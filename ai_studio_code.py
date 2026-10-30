# ==========================================
# 1. FUNÇÕES DAS OPERAÇÕES MATEMÁTICAS
# ==========================================

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Proteção contra divisão por zero
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b


# ==========================================
# 2. INTERFACE COM O USUÁRIO
# ==========================================

print("=== CALCULADORA SIMPLES ===")
print("Escolha a operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Recebe a escolha do usuário
opcao = input("Digite o número da operação (1/2/3/4): ")

# Verifica se a opção digitada é válida
if opcao in ['1', '2', '3', '4']:
    # Recebe os números e converte para número decimal (float)
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza a operação com base na escolha
    if opcao == '1':
        print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
    elif opcao == '2':
        print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
    elif opcao == '3':
        print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
    elif opcao == '4':
        resultado = dividir(num1, num2)
        print(f"Resultado: {resultado}")

else:
    print("Opção inválida! Por favor, execute o programa novamente e escolha de 1 a 4.")