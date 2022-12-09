from copy import deepcopy

moves = []
pos_head = [0, 0]
pos_tail = [0, 0]
hist_head = [0, 0]
history = []


def step(direction, rope):
    if direction == 'R':
        rope[0] += 1
    if direction == 'L':
        rope[0] -= 1
    if direction == 'U':
        rope[1] += 1
    if direction == 'D':
        rope[1] -= 1
    return rope


def move_head(direction):
    global hist_head, pos_head, pos_tail
    pos_head = step(direction, pos_head)

    if abs(pos_head[0]-pos_tail[0]) > 1 or abs(pos_head[1]-pos_tail[1]) > 1:
        pos_tail = hist_head
        if pos_tail not in history:
            history.append(pos_tail)
    hist_head = deepcopy(pos_head)


if __name__ == '__main__':
    with open('input_test_big') as f:
        lines = f.read().splitlines()
        for line in lines:
            direction, steps = line.split(' ')

            for _ in range(int(steps)):
                moves.append(direction)

    for move in moves:
        move_head(move)

    print(moves)
    print(len(history)+1)
