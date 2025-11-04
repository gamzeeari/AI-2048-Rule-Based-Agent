from game_logic import Board, SIZE
import random

def heuristic(board):
    empty = sum(1 for r in range(SIZE) for c in range(SIZE) if board.grid[r][c]==0)
    max_tile = max(max(row) for row in board.grid)
    return empty*200 + max_tile*5 + board.score

def ai_move(board):
    moves = ['up','down','left','right']
    best = None
    best_score = -1e9

    for move in moves:
        clone = board.clone()
        if not clone.move(move):
            continue
        clone.add_random()
        score = heuristic(clone)
        if score > best_score:
            best_score = score
            best = move
    return best
