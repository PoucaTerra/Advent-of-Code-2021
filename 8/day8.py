f = open("input.txt", "r")
lines = f.read().splitlines()

lines = list(map(lambda x: x.split("|"), lines))

lines = list(map(lambda x: x[1], lines))

lines = list(map(lambda x: x.split(), lines))

lines = sum(lines, [])

count = 0

for word in lines:
    length = len(word)
    if length == 2 or length == 3 or length == 4 or length == 7:
        count += 1

print(count)
