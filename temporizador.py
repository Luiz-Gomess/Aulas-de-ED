import time

class Temporizador:
    def __init__(self) :
        self.duracao = 0

    def setDuracao(self,novoDuracao):
        self.duracao = novoDuracao

    def iniciarContagem(self):
        for t in range(self.duracao,0,-1):
            print(f'{t} seg')
            time.sleep(1)




timer = Temporizador()
timer.setDuracao(10)
timer.iniciarContagem()
