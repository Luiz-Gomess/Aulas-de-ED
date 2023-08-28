class BombaCombus:
    def __init__(self) -> None:
        self.preco_litro = 5

    def totalPagar(self,litros):
        total = self.preco_litro * litros
        return total
    

carro1 = BombaCombus()
print(carro1.totalPagar(10))
