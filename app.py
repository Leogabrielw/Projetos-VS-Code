# Função para verificar se um número é par ou ímpar
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Função principal
def main():
    try:
        numero = int(input("Digite um número: "))
        resultado = verificar_par_ou_impar(numero)
        print(f"O número {numero} é {resultado}.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Chamando a função principal
if __name__ == "__main__":
    main()
