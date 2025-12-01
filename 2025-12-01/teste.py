import random


lstValores = list()
valor = 0

#while len(lstValores) < 20:
lstValores = [valor for valor in range (0, 100,) if len(lstValores) < 20  ]
print(lstValores)