def converter_dolar_para_real(cotacao, dolares):
    dolares = reais / cotacao
    return dolares

def main():
    try:
        cotacao = float(input("Informe o valor da cotação do dólar: "))
        reais = float(input("Informe a quantidade de reais disponível: "))
        
        dolares_convertidos = converter_dolar_para_real(cotacao, reais)
        
        print(f"O valor de {reais:.2f} dólares em reais é: R$ {dolares_convertidos:.2f}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

main()