class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass

    def info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Carro(Veiculo):
    def acelerar(self):
        return "Carro acelerou"

    def frear(self):
        return "Carro freou"

class Moto(Veiculo):
    def acelerar(self):
        return "Moto acelerou"

    def frear(self):
        return "Moto freou"

class Bicicleta(Veiculo):
    def acelerar(self):
        return "Bicicleta acelerou"

    def frear(self):
        return "Bicicleta freou"

if __name__ == "__main__":
    veiculo1 = Carro("Toyota", "Corolla")
    veiculo2 = Moto("Honda", "CBR 1000")
    veiculo3 = Bicicleta("Trek", "X-Caliber")

    # Polimorfismo em ação
    veiculos = [veiculo1, veiculo2, veiculo3]

    for veiculo in veiculos:
        print(f"{veiculo.info()}: {veiculo.acelerar()}")
        print(f"{veiculo.info()}: {veiculo.frear()}")
        print()