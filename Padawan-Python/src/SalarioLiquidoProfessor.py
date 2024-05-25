def calcular_salario_liquido(valor_hora_aula, horas_trabalhadas, percentual_desconto):
    salario_bruto = valor_hora_aula * horas_trabalhadas
    desconto = (percentual_desconto / 100) * salario_bruto
    salario_liquido = salario_bruto - desconto
    return salario_bruto, salario_liquido

def main():
    try:
        valor_hora_aula = float(input("Informe o valor da hora-aula: "))
        horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
        percentual_desconto = float(input("Informe o percentual de desconto do INSS: "))
        
        salario_bruto, salario_liquido = calcular_salario_liquido(valor_hora_aula, horas_trabalhadas, percentual_desconto)
        
        print(f"Salário Bruto: R$ {salario_bruto:.2f}")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

main()