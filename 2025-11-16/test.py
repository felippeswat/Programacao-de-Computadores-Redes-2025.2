# Mini teste da linha mágica
LIMITE = 1000

for n in [1, 5, 560]:
    S = n * (n + 1) // 2
    limite_m = min(LIMITE, S)
    print(f"n={n}, S={S}, limite_m={limite_m} → testa m de 1 até {limite_m}")