from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')

bebida_suco = Bebida('Suco de maçã', 12.90, 'Grande')
bebida_suco.aplicar_desconto()

prato_taco = Prato('Taco', 15, 'Taco original')
prato_taco.aplicar_desconto()

restaurante_mexicano.adicionar_item_cardapio(bebida_suco)
restaurante_mexicano.adicionar_item_cardapio(prato_taco)

def main():
    restaurante_mexicano.exibir_cardapio

if __name__ == '__main__':
    main()