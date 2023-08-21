from Temporizador import Temporizador

class Semaforo:
    def __init__(self):
        self.estadoAtual = 1
        self.timer = Temporizador()
        self.tempoDeTransição = {1:20,2:5,3:10}
        
