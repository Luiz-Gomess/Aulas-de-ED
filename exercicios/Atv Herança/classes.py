class NPC:
    def __init__(self,campeao,time,defesa,ataque,magia,alcance):
        self.campeao = campeao
        self.time = time
        self.ataque =  ataque
        self.defesa = defesa
        self.alcance = alcance
        self.magia = magia
        self.estado = True

    def info(self):
        print(f"""
--------------------
Campeão:.........{self.campeao}
Time:............{self.time}
Ataque:..........{self.ataque}
Defesa:..........{self.defesa}
Magia:...........{self.magia}
Alcance:.........{self.alcance}
Estado:..........{"Vivo" if self.estado else "Morto"}
--------------------
        """)

class Guerreiro(NPC):
    def __init__(self,campeao,time):
        self.ataque =  200
        self.defesa = 100
        self.magia = 10
        self.alcance = "melee"
        super().__init__(campeao,time,self.ataque,self.defesa,self.magia,self.alcance)

class Atirador(NPC):
    def __init__(self,campeao,time):
        self.nada = 20
        self.ataque =  300
        self.defesa =  50
        self.magia = 20
        self.alcance = "ranged"
        super().__init__(campeao,time,self.ataque,self.defesa,self.magia,self.alcance)

class Mago(NPC):
    def __init__(self,campeao,time):
        self.ataque = 50
        self.defesa = 50
        self.magia = 200
        self.alcance = "ranged"
        super().__init__(campeao,time,self.ataque,self.defesa,self.magia,self.alcance)





