def AjusteSalarial():
    salario = float(input("Digite o valor do salário mensal: "))
    percent = float(input("Digite o valor do percentual do reajuste (em %): "))

    novo_salario = salario + (salario * percent / 100)

    print(f"O novo salário, após o reajuste de {percentual_reajuste}%, é: R$ {novo_salario:.2f}")

AjusteSalarial()