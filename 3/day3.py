f = open("input.txt", "r")

lines = f.read().splitlines()

number_count = len(lines)
line_size = len(lines[0])
lst = [0] * line_size

print(line_size)


for s in lines:
    for x in range(0, line_size):
        if s[x] == "1":
            lst[x] += 1

gamma_rate = ""
epsilon_rate = ""

for x in range(0, line_size):
    if(lst[x] > number_count/2):
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(epsilon_rate * gamma_rate)
