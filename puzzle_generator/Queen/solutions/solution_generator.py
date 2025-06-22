def solutions(size: int):
    board = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            board = place_queen(board, x, y, size)

            #TODO: Implement backtracking logic to explore all possible solutions

            print(board)
            break
        break

def place_queen(board: list[list[int]], x: int, y: int, size: int) -> list[list[int]]:
    board[y][x] = 1
    for _y in range(size):
        if board[_y][x] == 0:
            board[_y][x] = -1
    for _x in range(size):
        if board[y][_x] == 0:
            board[y][_x] = -1
    if y+1<=4 and x+1<=4: board[y+1][x+1] = -1
    if y-1>=0 and x+1<=4: board[y-1][x+1] = -1
    if y+1<=4 and x-1>=0: board[y+1][x-1] = -1
    if y-1>=0 and x-1>=0: board[y-1][x-1] = -1
    return board

if __name__ == "__main__":
    solutions(5)