def soma_pares(inicio, fim):
    soma = 0
    
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            soma += num
    return soma

def main():


    try:
        inicio = int(input("Informe o número inicial do intervalo: "))
        fim = int(input("Informe o número final do intervalo: "))
    
        if fim < inicio:
            print("O número final deve ser maior ou igual ao número inicial. Programa encerrado.")
        else:
            soma = soma_pares(inicio, fim)
            print(f"A soma dos números pares no intervalo de {inicio} a {fim} é {soma}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

main()