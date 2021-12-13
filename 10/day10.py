f = open("input.txt", "r")
lines = f.read().splitlines()

points = {')': 1,
          ']': 2,
          '}': 3,
          '>': 4}

pairs = {'(': ')',
         '[': ']',
         '{': '}',
         '<': '>'}

pairs2 = {')': '(',
          ']': '[',
          '}': '{',
          '>': '<'}


scores = []

for l in lines:

    stack = []
    score = 0
    corrupt = False

    for c in l:
        if c in pairs2.keys():
            pair = stack.pop()
            if pair != pairs2.get(c):
                corrupt = True
                break
        else:
            stack.append(c)

    if not(corrupt) and len(stack) != 0:
        stack.reverse()
        for c in stack:
            score *= 5
            score += points.get(pairs.get(c))

        scores.append(score)


scores.sort()
print(scores)
print(scores[len(scores)//2])
