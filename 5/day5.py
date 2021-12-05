f = open("input_test.txt", "r")
lines = f.read().splitlines()

lines = list(map(lambda x: x.split(), lines))
lines = list(map(lambda x: (x[0], x[2]), lines))
lines = list(map(lambda x: ((int(x[0].split(",")[0]), int(x[0].split(",")[
             1])), (int(x[1].split(",")[0]), int(x[1].split(",")[1]))), lines))

lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines))

possible = []


for l in lines:
    if l[0][0] == l[1][0]:
        points = [(l[0][0], x)
                  for x in range(min(l[0][1], l[1][1]), max(l[0][1], l[1][1])+1)]

        possible = possible + points

    if l[0][1] == l[1][1]:
        points = [(x, l[1][1])
                  for x in range(min(l[0][0], l[1][0]), max(l[0][0], l[1][0])+1)]

        possible = possible + points

count = 0
dict = {}

while(len(possible) > 0):
    elem = possible.pop(0)
    dict[elem] = dict[elem] + 1 if elem in dict else 1

for p in dict:
    if dict[p] >= 2:
        count += 1

print(count)
