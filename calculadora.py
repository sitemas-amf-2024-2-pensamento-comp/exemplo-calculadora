# Função de menu para usuário escolher o que ele quer fazer
def mostraMenu():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. SAIR DO PROGRAMA")

def calcular(operador, num1, num2):
    # if-elif-else
    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1 - num2
    elif operador == 3:
        return num1 * num2
    elif operador == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro! Divisão por zero!"
    else:
        return "Saindo/encerrando programa..."

def main():
    while True:
        mostraMenu() # invocando o menu para aparecer na tela

        opcaoDigitada = int(input("Digite a opção desejada: "))
        # condicao para sair do programa
        if opcaoDigitada == 5:
            print("Saindo do programa...")
            break
        # lendo os dois números digitados pelo usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # chamando a função calcular
        resultado = calcular(opcaoDigitada, num1, num2)
        # Resultado da operação
        print(f"O resultado é: {resultado}")
        # Checagem para ver se usuário quer continuar ou não
        continuaOuNao = input("Deseja continuar? (s/n): ")
        # condição para sair ou não do programa
        if continuaOuNao.lower() != 's':
            print("Obrigado por usar a calculadora. Encerrando...")
            break

if __name__ == "__main__":
    main()
