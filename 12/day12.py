f = open("input.txt", "r")
lines = f.read().splitlines()

dict = {}


def findPath(cave, path, dict):
    opts = dict[cave]
    paths = []
    current_path = path.copy()
    current_path.append(cave)

    if cave == "end":
        return current_path

    for c in opts:

        if c.islower() and c in path:
            continue

        else:
            new_paths = findPath(c, current_path, dict)
            if new_paths and all(isinstance(elem, str) for elem in new_paths):
                paths.append(new_paths)

            else:
                if new_paths:
                    paths = paths + new_paths

    return paths


for connection in lines:
    caves = connection.split("-")
    if not (caves[0] in dict):
        dict[caves[0]] = [caves[1]]
    else:
        dict[caves[0]].append(caves[1])

    if not (caves[1] in dict):
        dict[caves[1]] = [caves[0]]
    else:
        dict[caves[1]].append(caves[0])


paths = findPath("start", [], dict)

print(paths)

print(len(paths))
