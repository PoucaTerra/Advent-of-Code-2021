f = open("input.txt", "r")


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.marked = [[False for x in range(5)] for y in range(5)]


order = list(map(lambda x: int(x), f.readline().split(",")))
grids: list[Grid] = []

line = f.readline()

while(line):
    grid = []
    for i in range(0, 5):
        grid.append(list(map(lambda x: int(x), f.readline().split())))

    grids.append(Grid(grid))
    line = f.readline()


def game(order, grids, won):
    for n in order:
        for g in range(0, len(grids)):
            if(won[g]):
                continue
            for i in range(0, 5):
                for x in range(0, 5):
                    if(grids[g].grid[i][x] == n):
                        grids[g].marked[i][x] = True
                        if(all(grids[g].marked[i])):
                            won[g] = True
                            if(all(won)):
                                return (n, grids[g])
                        if all([sub[x] for sub in grids[g].marked]):
                            won[g] = True
                            if(all(won)):
                                return (n, grids[g])


last: tuple[int, Grid] = game(order, grids, list(map(lambda x: False, grids)))

sum = 0

for i in range(0, 5):
    for x in range(0, 5):
        if not(last[1].marked[i][x]):
            sum += last[1].grid[i][x]

print(last[0]*sum)
