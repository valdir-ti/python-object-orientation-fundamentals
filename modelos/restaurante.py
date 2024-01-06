from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    '''Construtor da classe'''
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    '''Retorno padrão ao chamar a classe'''
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    '''Utilizando um classmethod para acessar métodos da classe'''
    '''Listando os restaurantes'''    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"NOME DO RESTAURANTE".ljust(20)} | {"CATEGORIA".ljust(20)} | {"AVALIAÇÃO".ljust(20)} | {"STATUS".ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo.ljust(20)}')
    
    '''Property'''
    '''Acessando uma propriedade da classe e definindo um retorno'''
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    '''Alternando estado'''
    def alternar_estado(self):
        self._ativo = not self._ativo

    '''Faz a avaliação de um restaurante'''
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    '''Realizando a media das notas do restaurante'''
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        somas_das_notas  = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(somas_das_notas/quantidade_de_notas, 1)
        return media