f = open("input.txt", "r")

lines = f.readlines()

"""

# First

depth = 0
x = 0

for l in lines:
    line = l.split(" ")

    if(line[0] == "forward"):
        x += int(line[1])

    if(line[0] == "down"):
        depth += int(line[1])

    if(line[0] == "up"):
        depth -= int(line[1])

print(depth*x)
"""

# Second

aim = 0
depth = 0
x = 0

for l in lines:
    line = l.split(" ")

    if(line[0] == "forward"):
        x += int(line[1])
        depth += int(line[1])*aim

    if(line[0] == "down"):
        aim += int(line[1])

    if(line[0] == "up"):
        aim -= int(line[1])

print(depth*x)
