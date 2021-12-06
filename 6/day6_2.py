f = open("input.txt", "r")
line = f.readline().split(",")

fish = list(map(lambda x: int(x), line))

dict = {}

for i in range(0, 9):
    dict[i] = fish.count(i)

for i in range(0, 256):
    print(dict)
    new_dict = {}
    for i in range(0, 8):
        if i == 0:
            new_dict[8] = dict[0]
        if i == 6:
            new_dict[6] = dict[0] + dict[7]
        else:
            new_dict[i] = dict[i+1]

    dict = new_dict

print(sum(dict.values()))
