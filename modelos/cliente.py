class Cliente:
    def __init__(self, nome, email, idade, telefone) -> None:
        self.nome = nome
        self.email = email
        self.idade = idade
        self.telefone = telefone

    def __str__(self) -> str:
        return f'{self.nome} | {self.idade} | {self.email} | {self.telefone}'
    
cliente1 = Cliente('Valdir', 'val@mail.com', 42, '5555-4443')
cliente2 = Cliente('Julia', 'ju@mail.com', 17, '3333-4112')

clientes = [cliente1, cliente2]

print(cliente1)
print(cliente2)