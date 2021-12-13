class Solution:
    def __init__(self):
        self.step = 0
        f = open("input.txt", "r")
        self.lines = f.read().splitlines()
        self.lines = list(map(lambda x: [int(char) for char in x], self.lines))

        self.lines.append([-1 for i in self.lines[0]])
        self.lines.insert(0, [-1 for i in self.lines[0]])

        for l in self.lines:
            l.append(-1)
            l.insert(0, -1)

        self.flashed = set()
        self.flashes = 0

    def flash(self, x, y):
        if ((x, y) in self.flashed) or self.lines[x][y] == -1:
            return
        self.lines[x][y] += 1
        if self.lines[x][y] > 9:
            self.flashed.add((x, y))
            self.flashes += 1
            self.lines[x][y] = 0
            self.flash(x + 1, y)
            self.flash(x - 1, y)
            self.flash(x, y + 1)
            self.flash(x, y - 1)
            self.flash(x + 1, y + 1)
            self.flash(x - 1, y - 1)
            self.flash(x + 1, y - 1)
            self.flash(x - 1, y + 1)

    def run(self):
        while True:
            self.step += 1
            for x in range(1, len(self.lines) - 1):
                for y in range(1, len(self.lines[0]) - 1):
                    self.flash(x, y)

            if len(self.flashed) == (len(self.lines) - 2) * (len(self.lines[0]) - 2):
                return
            self.flashed.clear()


solution = Solution()
solution.run()
print(solution.step)
