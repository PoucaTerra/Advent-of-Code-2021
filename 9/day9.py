f = open("input.txt", "r")
lines = f.read().splitlines()
lines = list(map(lambda x: [int(char) for char in x], lines))
lines.append([10 for i in lines[0]])
lines.insert(0, [10 for i in lines[0]])
sum = 0

for l in lines:
    l.append(10)
    l.insert(0, 10)

for i in range(1, len(lines)-1):
    for x in range(1, len(lines[0])-1):
        current = lines[i][x]
        top = lines[i+1][x]
        bottom = lines[i-1][x]
        left = lines[i][x-1]
        right = lines[i][x+1]
        if(current < top and current < bottom and current < left and current < right):
            sum += 1 + current

print(sum)
