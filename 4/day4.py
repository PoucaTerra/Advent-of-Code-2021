f = open("input_test.txt", "r")


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


def game(order, grids):
    for n in order:
        for g in grids:
            for i in range(0, 5):
                for x in range(0, 5):
                    if(g.grid[i][x] == n):
                        g.marked[i][x] = True
                        if(all(g.marked[i])):
                            return (n, g)
                        if all([sub[x] for sub in g.marked]):
                            return (n, g)


last: tuple[int, Grid] = game(order, grids)

sum = 0

for i in range(0, 5):
    for x in range(0, 5):
        if not(last[1].marked[i][x]):
            sum += last[1].grid[i][x]

print(sum)
print(last[0]*sum)
