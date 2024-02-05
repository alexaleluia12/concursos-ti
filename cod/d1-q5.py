
def verifica(a, b, c):
    if a * 2 == c:
        return b + 1
    elif b / 2 == c:
        return b - 1

    return 0

a = verifica(2, 0, 4)
b = verifica(1, 2, 3)
c = verifica(0, 4, 2)
print(a, b, c)
