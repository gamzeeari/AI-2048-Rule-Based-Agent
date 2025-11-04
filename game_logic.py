import random

SIZE = 4

class Board:
    def __init__(self):
        self.grid = [[0]*SIZE for _ in range(SIZE)]
        self.score = 0
        self.add_random()
        self.add_random()

    def clone(self):
        b = Board()
        b.grid = [row[:] for row in self.grid]
        b.score = self.score
        return b

    def add_random(self):
        empty = [(r,c) for r in range(SIZE) for c in range(SIZE) if self.grid[r][c]==0]
        if not empty: return False
        r,c = random.choice(empty)
        self.grid[r][c] = 4 if random.random() < 0.1 else 2
        return True

    def can_move(self):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.grid[r][c] == 0:
                    return True
        for r in range(SIZE):
            for c in range(SIZE-1):
                if self.grid[r][c] == self.grid[r][c+1]:
                    return True
        for c in range(SIZE):
            for r in range(SIZE-1):
                if self.grid[r][c] == self.grid[r+1][c]:
                    return True
        return False

    def move(self, direction):
        moved = False
        if direction == 'left':
            for r in range(SIZE):
                moved |= self.compress_merge(r)
        elif direction == 'right':
            for r in range(SIZE):
                self.grid[r].reverse()
                moved |= self.compress_merge(r)
                self.grid[r].reverse()

        elif direction == 'up':
            for c in range(SIZE):
                col = [self.grid[r][c] for r in range(SIZE)]
                tiles = self.merge_list(col)
                for r in range(SIZE):
                    if self.grid[r][c] != tiles[r]:
                        moved = True
                    self.grid[r][c] = tiles[r]

        elif direction == 'down':
            for c in range(SIZE):
                col = [self.grid[r][c] for r in range(SIZE)][::-1]
                tiles = self.merge_list(col)[::-1]
                for r in range(SIZE):
                    if self.grid[r][c] != tiles[r]:
                        moved = True
                    self.grid[r][c] = tiles[r]
        return moved

    def compress_merge(self, r):
        tiles = [v for v in self.grid[r] if v != 0]
        merged = []
        i = 0
        while i < len(tiles):
            if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
                merged.append(tiles[i] * 2)
                self.score += tiles[i] * 2
                i += 2
            else:
                merged.append(tiles[i])
                i += 1
        merged += [0] * (SIZE - len(merged))
        changed = merged != self.grid[r]
        self.grid[r] = merged
        return changed

    def merge_list(self, lst):
        tiles = [v for v in lst if v != 0]
        merged = []
        i = 0
        while i < len(tiles):
            if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
                merged.append(tiles[i] * 2)
                self.score += tiles[i] * 2
                i += 2
            else:
                merged.append(tiles[i])
                i += 1
        merged += [0] * (SIZE - len(merged))
        return merged
