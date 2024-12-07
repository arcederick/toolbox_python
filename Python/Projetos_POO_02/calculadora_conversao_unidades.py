class CalculadoraConversao:
    def converter_celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def converter_fahrenheit_para_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def converter_quilometros_para_milhas(self, quilometros):
        return quilometros * 0.621371

    def converter_milhas_para_quilometros(self, milhas):
        return milhas / 0.621371

calculadora = CalculadoraConversao()

while True:
    print("Calculadora de Conversão de Unidades")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celsius")
    print("3. Converter Quilômetros para Milhas")
    print("4. Converter Milhas para Quilômetros")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = calculadora.converter_celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius equivalem a {resultado} graus Fahrenheit.")
    elif escolha == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = calculadora.converter_fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit equivalem a {resultado} graus Celsius.")
    elif escolha == "3":
        quilometros = float(input("Digite a distância em Quilômetros: "))
        resultado = calculadora.converter_quilometros_para_milhas(quilometros)
        print(f"{quilometros} quilômetros equivalem a {resultado} milhas.")
    elif escolha == "4":
        milhas = float(input("Digite a distância em Milhas: "))
        resultado = calculadora.converter_milhas_para_quilometros(milhas)
        print(f"{milhas} milhas equivalem a {resultado} quilômetros.")
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")