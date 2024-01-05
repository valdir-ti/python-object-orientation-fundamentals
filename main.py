from modelos.restaurante import Restaurante

restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')
restaurante_mexicano.alternar_estado()
restaurante_macarroni = Restaurante('Macarroni', 'Comida Italiana')
restaurante_outback = Restaurante('outback', 'Comida Australiana')
restaurante_outback.alternar_estado()


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()