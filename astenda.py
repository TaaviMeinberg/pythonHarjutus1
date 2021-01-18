def astenda(arv, aste):
    tulemus = 1
    for üksAste in range(1, aste+1):
        tulemus = arv * tulemus
    return tulemus

print(astenda(5,5))

print(astenda(10,5))