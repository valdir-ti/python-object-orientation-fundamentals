from modelos.restaurante import Restaurante

restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')
restaurante_mexicano.alternar_estado()
restaurante_mexicano.receber_avaliacao('Valdir Silva', 6)
restaurante_mexicano.receber_avaliacao('Julia Felix', 8)
restaurante_mexicano.receber_avaliacao('Julia Felix', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()