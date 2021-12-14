from itertools import groupby

f = open("input.txt", "r")
lines = f.read().splitlines()
rules = lines[2:]
rules = list(map(lambda x: (x.split(" -> ")[0], x.split(" -> ")[1]), rules))
template = lines[0]
rules = dict(rules)

pairs_count = {}

for i in range(0, len(template) - 1):
    if str(template[i : i + 2]) in pairs_count:
        pairs_count[str(template[i : i + 2])] = (
            pairs_count[str(template[i : i + 2])] + 1
        )

    else:
        pairs_count[str(template[i : i + 2])] = 1

for n in range(0, 40):
    new_pairs_count = {}
    print(pairs_count)

    for rule in rules:
        print(rule + " -> " + rules[rule])

        if rule in pairs_count:
            pair_left = rule[0] + rules[rule]
            pair_right = rules[rule] + rule[1]
            count = pairs_count[rule]
            pairs_count[rule] = 0

            if pair_left in new_pairs_count:
                new_pairs_count[pair_left] = new_pairs_count[pair_left] + count
            else:
                new_pairs_count[pair_left] = count

            if pair_right in new_pairs_count:
                new_pairs_count[pair_right] = new_pairs_count[pair_right] + count
            else:
                new_pairs_count[pair_right] = count

    for pair in pairs_count:
        if pair in new_pairs_count:
            new_pairs_count[pair] = new_pairs_count[pair] + pairs_count[pair]
        else:
            new_pairs_count[pair] = pairs_count[pair]

    pairs_count = new_pairs_count.copy()

letter_count = dict()

for pair in pairs_count:
    l1 = pair[0]
    l2 = pair[1]
    if l1 in letter_count:
        letter_count[l1] = letter_count[l1] + pairs_count[pair]
    else:
        letter_count[l1] = pairs_count[pair]

    if l2 in letter_count:
        letter_count[l2] = letter_count[l2] + pairs_count[pair]
    else:
        letter_count[l2] = pairs_count[pair]

counter = list(letter_count.values())

counter = list(map(lambda x: ((x + 1) // 2), counter))
counter.sort()

print(counter[len(counter) - 1] - counter[0])
