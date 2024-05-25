def fizz_buzz(inicio, fim):
    for num in range(inicio, fim + 1):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)  

def main():
    try:
        inicio = int(input("Informe o número inicial do intervalo: "))
        fim = int(input("Informe o número final do intervalo: "))
        
        if fim <= inicio:
            print("O número final deve ser maior que o número inicial. Programa encerrado.")
        else:
            fizz_buzz(inicio, fim)
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

main()