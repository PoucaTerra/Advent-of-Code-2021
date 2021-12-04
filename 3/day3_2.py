f = open("input_test.txt", "r")

lines = f.read().splitlines()
lst = lines
line_size = len(lines[0])

result = 1

for i in range(0, line_size):
    lst_0 = []
    lst_1 = []

    count = 0

    for s in lst:
        if s[i] == "1":
            lst_1.append(s)
        else:
            lst_0.append(s)

    lst = lst_1 if len(lst_1) >= len(lst_0) else lst_0

    if len(lst) == 1:
        result *= int(lst[0], 2)
        break

lst = lines

for i in range(0, line_size):
    lst_0 = []
    lst_1 = []

    count = 0

    for s in lst:
        if s[i] == "1":
            lst_1.append(s)
        else:
            lst_0.append(s)

    lst = lst_1 if len(lst_1) < len(lst_0) else lst_0

    if len(lst) == 1:
        result *= int(lst[0], 2)
        break

print(result)
