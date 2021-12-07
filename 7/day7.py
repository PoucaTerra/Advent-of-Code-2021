import sys

f = open("input.txt", "r")
line = f.readline().split(",")

line = list(map(lambda x: int(x), line))
line.sort()
cost = sys.maxsize

for i in range(0, line[len(line)-1]):

    current_cost = 0

    for x in range(0, len(line)):

        current_cost += sum(range(abs(i - line[x])+1))

    if current_cost < cost:

        cost = current_cost

print(cost)
