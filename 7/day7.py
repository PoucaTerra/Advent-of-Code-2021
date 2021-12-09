f = open("input.txt", "r")
line = f.readline().split(",")

line = list(map(lambda x: int(x), line))
line.sort()


def calculate_cost(target, positions):
    result = 0

    for x in range(0, len(positions)):

        result += abs(target - positions[x])

    return result


middle = line[len(line)-1] // 2
cost = 0


if calculate_cost(middle-1, line) < calculate_cost(middle, line):

    i = middle - 1
    cost = calculate_cost(middle, line)
    while(i >= 0 and calculate_cost(i - 1, line) < cost):
        cost = calculate_cost(i - 1, line)
        i -= 1

else:
    if calculate_cost(middle+1, line) < calculate_cost(middle, line):
        i = middle + 1
        cost = calculate_cost(middle, line)
        while(i <= line[len(line)-1] and calculate_cost(i + 1, line) < cost):
            cost = calculate_cost(i + 1, line)
            i += 1

    else:
        cost = calculate_cost(middle, line)

print(cost)
