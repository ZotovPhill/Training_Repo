import time


def list_comp_censored(censored, vowels):
    vowels_list = list(vowels)
    vowels_list.reverse()
    message = [vowels_list.pop() if letter == "*" else letter for letter in censored]
    return "".join(message)


def for_censored(censored, vowels):
    new = []
    vowels_list = list(vowels)
    vowels_list.reverse()
    for letter in censored:
        if letter == "*":
            a = vowels_list.pop()
            new.append(a)
        else:
            new.append(letter)
    return "".join(new)


def for_assighment_censored(censored, vowels):
    censored_list = list(censored)
    vowels_list = list(vowels)
    vowels_list.reverse()
    for index, letter in enumerate(censored_list):
        if letter != "*":
            continue
        else:
            a = vowels_list.pop()
            censored_list[index] = a
    return "".join(censored_list)


def show_time(start_time):
    runtime = time.time() - start_time
    return runtime


censored = "Wh*r* d*d my v*w*ls g*?"
vowels = "eeioeo"

print("List comprehension censored:")
start_time = time.time()
print(list_comp_censored(censored, vowels))
print(show_time(start_time), "\n")

print("For loop censored:")
start_time = time.time()
print(for_censored(censored, vowels))
print(show_time(start_time), "\n")

print("For assignment loop:")
start_time = time.time()
print(for_assighment_censored(censored, vowels))
print(show_time(start_time), "\n")
