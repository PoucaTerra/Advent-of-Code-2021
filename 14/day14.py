from itertools import groupby

f = open("input_test.txt", "r")
lines = f.read().splitlines()
rules = lines[2:]
rules = list(map(lambda x: (x.split(" -> ")[0], x.split(" -> ")[1]), rules))
template = lines[0]
rules = dict(rules)

for n in range(0, 10):
    new_template = ""

    for i in range(0, len(template) - 1):
        if str(template[i : i + 2]) in rules:
            new_template += template[i] + rules[str(template[i : i + 2])]
        else:
            new_template += template[i]

    new_template += template[len(template) - 1]

    template = new_template

template = [c for c in template]
template.sort()

counter = [len(list(group)) for key, group in groupby(template)]
counter.sort()

print(counter[len(counter) - 1] - counter[0])
