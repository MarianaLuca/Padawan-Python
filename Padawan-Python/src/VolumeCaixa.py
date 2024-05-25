def CalcularVolume(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume

def main():
    try:
        comprimento = float(input("Informe o comprimento da caixa: "))
        largura = float(input("Informe a largura da caixa: "))
        altura = float(input("Informe a altura da caixa: "))

        volume = calcular_volume(comprimento, largura, altura)

        println(f"O volume da caixa retangular é: {volume:.2f} metros cúbicos")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")     

main()
