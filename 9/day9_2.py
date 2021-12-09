f = open("input.txt", "r")
lines = f.read().splitlines()
lines = list(map(lambda x: [int(char) for char in x], lines))
lines.append([10 for i in lines[0]])
lines.insert(0, [10 for i in lines[0]])
sum = 0

for l in lines:
    l.append(10)
    l.insert(0, 10)

basins = []

for i in range(1, len(lines)-1):
    for x in range(1, len(lines[0])-1):
        current = lines[i][x]
        top = lines[i+1][x]
        bottom = lines[i-1][x]
        left = lines[i][x-1]
        right = lines[i][x+1]
        if(current < top and current < bottom and current < left and current < right):
            basin = 0
            stack = [(i, x)]
            seen = {(i, x)}
            while(stack):
                point = stack.pop()
                point_value = lines[point[0]][point[1]]
                if(point_value in {9, 10}):
                    continue

                basin += 1

                top = lines[point[0]+1][point[1]]
                bottom = lines[point[0]-1][point[1]]
                left = lines[point[0]][point[1]-1]
                right = lines[point[0]][point[1]+1]

                if(top > point_value and not((point[0]+1, point[1]) in seen)):
                    seen.add((point[0]+1, point[1]))
                    stack.append((point[0]+1, point[1]))

                if(bottom > point_value and not((point[0]-1, point[1]) in seen)):
                    seen.add((point[0]-1, point[1]))
                    stack.append((point[0]-1, point[1]))

                if(left > point_value and not((point[0], point[1]-1) in seen)):
                    seen.add((point[0], point[1]-1))
                    stack.append((point[0], point[1]-1))

                if(right > point_value and not((point[0], point[1]+1) in seen)):
                    seen.add((point[0], point[1]+1))
                    stack.append((point[0], point[1]+1))

            basins.append(basin)


basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
