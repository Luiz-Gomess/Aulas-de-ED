from enum import Enum
from temporizador import Temporizador


class Estado(Enum):
    Vermelho = 1
    Amarelo = 2
    Verde = 3


class SemaforoTemporizado:
    def __init__(self,estadoInicial:Estado = Estado.Vermelho):

        self.estadoAtual = estadoInicial
        self.timer = Temporizador()
        self.tempoDeTransição = {Estado.Verde:20,Estado.Amarelo:5,Estado.Vermelho:10}

    def getEstadoAtual(self)->Estado:
        return self.estadoAtual
    
    def __str__(self) -> str:
        return f'''
        +-------+
        |  ({"X" if self.estadoAtual == Estado.Vermelho else " "})  |
        |  ({"X" if self.estadoAtual == Estado.Amarelo else " "})  |
        |  ({"X" if self.estadoAtual == Estado.Verde else " "})  |
        +-------+
        '''
    def setup(self,tempoVermelho:int,tempoAmarelo:int,tempoVerde:int):
        """
        Método que permite ajustar o tempo dos estados do semáforo.
        Aceita um tempo em segundos entre 1 e 59

        Argumentos
        ----------
        tempoVermelho (int): tempo de segundos de permanência no vermelho
        tempoAmarelo (int): tempo de segundos de permanência no amarelo
        tempoVerde (int): tempo de segundos de permanência no verde
        """
        if tempoVermelho < 1 or tempoVermelho > 59:
            return
        if tempoAmarelo < 1 or tempoAmarelo > 59:
            return
        if tempoVerde < 1 or tempoVerde > 59:
            return

        self.tempoDeTransição[Estado.Vermelho] = tempoVermelho
        self.tempoDeTransição[Estado.Amarelo] = tempoAmarelo
        self.tempoDeTransição[Estado.Verde] = tempoVerde


    def start(self):
        self.timer.setDuracao(self.tempoDeTransição[self.estadoAtual])
        self.timer.iniciarContagem()