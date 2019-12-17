import pprint

layers = int(input("Enter layers count: "))
outer = []

for i in range(layers):
    n = 0
    inner = []
    while n <= layers - 1:
        if n <= i:
            inner.append("#")
            n += 1
        else:
            inner.append("-")
            n += 1
    outer.append(inner)
pprint.pprint(outer, width=120)

