class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def __str__(self) -> str:
        return f'{self.modelo} | {self.ano}'
            
carro = Carro('Ferrari', 'Vermelha', '1988')

print(carro)

