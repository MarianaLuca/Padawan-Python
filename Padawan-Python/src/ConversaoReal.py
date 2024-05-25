def converter_dolar_para_real(cotacao, dolares):
    reais = cotacao * dolares
    return reais

def main():
    try:
        cotacao = float(input("Informe o valor da cotação do dólar: "))
        dolares = float(input("Informe a quantidade de dólares disponível: "))
        
        reais_convertidos = converter_dolar_para_real(cotacao, dolares)
        
        print(f"O valor de {dolares:.2f} dólares em reais é: R$ {reais_convertidos:.2f}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

main()