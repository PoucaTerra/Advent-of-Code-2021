import copy

f = open("input.txt", "r")
lines = f.read().splitlines()

dict = {}


class Path:
    def __init__(self, path, hasLower):
        self.hasLower = hasLower
        self.path = path


def findPath(cave, path, dict):
    opts = dict[cave]
    paths = []
    p = path.path
    current_path = Path(p.copy(), path.hasLower)

    if cave.islower() and cave in current_path.path:
        current_path.path.append(cave)
        current_path.hasLower = True

    else:
        current_path.path.append(cave)

    if cave == "end":
        return current_path

    for c in opts:

        if c == "start":
            continue

        if c.islower() and c in current_path.path:
            if current_path.hasLower:
                continue
            else:
                new_paths = findPath(c, current_path, dict)
                if isinstance(new_paths, Path):
                    paths.append(new_paths)

                else:
                    if new_paths:
                        paths = paths + new_paths

        else:
            new_paths = findPath(c, current_path, dict)
            if isinstance(new_paths, Path):
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


paths = findPath("start", Path([], False), dict)

print(list(map(lambda x: (x.path, x.hasLower), paths)))

print(len(paths))
