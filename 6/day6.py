f = open("input_test.txt", "r")
line = f.readline().split(",")

fish = list(map(lambda x: int(x), line))

for i in range(0, 256):

    fish_updated = []
    for f in fish:
        if f == 0:
            fish_updated.append(8)
            fish_updated.append(6)
        else:
            fish_updated.append(f-1)

    fish = fish_updated

print(len(fish))

# Muito pouco eficiente, mas resulta para poucos dias
