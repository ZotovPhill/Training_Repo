def draw_line(space, stick=0, welcome=False):
    tilda = "-" * (space // 2 - 2)
    middle = "welcome" if welcome else ".|." * stick
    line = f"{tilda}{middle}{tilda}"
    return line


space = int(input("Введите длину строки: "))
rows = int(input("Введите количество строк: "))
new_row, new_space = rows, space
stick = 1
while rows != 0:
    if rows > new_row // 2 + 1:
        print(draw_line(space, stick))
        space -= 6
        stick += 2
    elif rows == new_row // 2 + 1:
        print(draw_line(new_space, welcome=True))
    else:
        welcome = False
        space += 6
        stick -= 2
        print(draw_line(space, stick))

    rows -= 1
