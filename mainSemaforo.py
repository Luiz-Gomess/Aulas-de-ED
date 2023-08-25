from Semaforo import SemaforoTemporizado, Estado

s1 = SemaforoTemporizado(Estado.Verde)
s2 = SemaforoTemporizado()

print(s1.getEstadoAtual())
print(s1)
print(s2)

print(s1.__dict__)
s1.setup(9,9,9)
print(s1)