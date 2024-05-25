def CalcularAreaCircunferencia(raio):
   pi =  3.14159265
   area = pi * (raio*2)
   return area 

def main():
    try:
        raio = float(input("Informe o valor do raio da circunferência: "))
        if raio < 0:
            print("O valor do raio deve ser um número positivo. Programa encerrado.")
        else:
            area = calcular_area_circunferencia(raio)
            print(f"A área da circunferência com raio {raio} é {area:.2f}")
    
    except ValueError:
        print("Por favor, insira um valor numérico válido para o raio.")

main()