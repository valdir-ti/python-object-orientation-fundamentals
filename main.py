from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')
bebida_suco = Bebida('Suco de maçã', 12.90, 'Grande')
prato_taco = Prato('Taco', 15.5, 'Taco original')
restaurante_mexicano.adicionar_item_cardapio(bebida_suco)
restaurante_mexicano.adicionar_item_cardapio(prato_taco)

def main():
    print(bebida_suco)
    print(prato_taco)

if __name__ == '__main__':
    main()