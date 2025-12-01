import random


lstValores = list()
valor = 0

#while len(lstValores) < 20:
lstValores = [ random.randint(1, 100) for _ in range (20)]
print(lstValores)