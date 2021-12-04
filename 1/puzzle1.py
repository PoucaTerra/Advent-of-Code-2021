import os

f = open('input.txt', "r")

numbers = list(map(int, f.read().splitlines()))
count = 0

# Prob 2
for x in range(1, len(numbers)-2):
    if(sum(numbers[x:x+3]) > sum(numbers[x-1:x+2])):
        count += 1

"""
# Prob 1
for x in range(1, len(sums)):
    if(sums[x] > sums[x-1]):
        count += 1

"""

print(count)
