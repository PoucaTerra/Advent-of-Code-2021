f = open("input.txt", "r")
lines = f.read().splitlines()
folds = []

line = lines.pop()

while line:
    folds.append(line)
    line = lines.pop()

folds.reverse()
folds = list(map(lambda x: x[11:], folds))

lines = list(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), lines))

while folds:
    fold = folds.pop(0)
    if fold[0] == "y":
        axis = int(fold[2:])
        above = set(filter(lambda x: x[1] < axis, lines))
        below = list(filter(lambda x: x[1] > axis, lines))
        below = list(map(lambda x: (x[0], axis - (x[1] - axis)), below))
        above.update(below)
        lines = above

    if fold[0] == "x":
        axis = int(fold[2:])
        left = set(filter(lambda x: x[0] < axis, lines))
        right = list(filter(lambda x: x[0] > axis, lines))
        right = list(map(lambda x: (axis - (x[0] - axis), x[1]), right))
        left.update(right)
        lines = left


def print_string(dots):
    x_max = max(dot[0] for dot in dots)
    y_max = max(dot[1] for dot in dots)
    grid = [["."] * (x_max + 1) for _ in range(y_max + 1)]

    for dot in dots:
        grid[dot[1]][dot[0]] = "#"

    for line in grid:
        print("".join(line))
    print()


print_string(lines)
