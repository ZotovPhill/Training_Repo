n = int(input("Введите количесво уровней елки: \n"))
branch = 1
while n != 0:
    layer = f"{' '*(n-1)}{'^'*branch}"
    print(layer)
    n -= 1
    branch += 2
bottom = f"{' '*(branch//2 -2)}| |"
print(bottom)
