def open_close_bracket(brackets_line):
    flags = []
    for i in brackets_line:
        if i == "(":
            flags.append(False)
        elif i == ")":
            try:
                flags.pop()
            except IndexError:
                return False
        else:
            continue
    if False in flags or flags != []:
        return False
    else:
        return True


def alternative_bracket(brackets_line):
    count = 0
    for char in brackets_line:
        if count < 0:
            return False
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
    return True if count == 0 else False


print(open_close_bracket(" (g)(s()))(n))"))
print(alternative_bracket(" (g)(s()))(n))"))

