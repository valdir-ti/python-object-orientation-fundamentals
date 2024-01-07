from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    '''Definindo uma classe abstrata'''
    @abstractmethod
    def aplicar_desconto(self):
        pass