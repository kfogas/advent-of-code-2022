import queue
import re
from typing import List


def stacking(moves, crates, part1) -> str:
    ret = ''
    queue_list = init_crates(crates)
    for move in moves:
        numbers = list(map(int, re.findall('[0-9]+', move)))

        if part1:
            for i in range(numbers[0]):
                queue_list[numbers[2]].put(queue_list[numbers[1]].get())
        else:
            for i in range(numbers[0]):
                queue_list[0].put(queue_list[numbers[1]].get())

            for i in range(numbers[0]):
                queue_list[numbers[2]].put(queue_list[0].get())

    for i in range(1, len(queue_list)):
        ret += queue_list[i].get()

    return ret


def init_crates(crates: str) -> List:
    queue_list = []
    lines = crates.split('\n')
    max_column = int(lines[-1][-2])
    max_rows = len(lines)-1

    # Placeholder for stacking and correct indexing
    temp_queue = queue.LifoQueue()
    temp_queue.put('Temporary Docking Station')
    queue_list.append(temp_queue)

    for i in range(max_column):

        q = queue.LifoQueue()
        queue_list.append(q)

        for j in range(2, max_rows + 2):
            char = lines[-j][1+4*i]
            if char.isalpha():
                q.put(char)

    return queue_list


if __name__ == '__main__':

    with open('input') as f:
        data = f.read()
        crates, movelist = data.split('\n\n')
        moves = movelist.split('\n')

        q1 = stacking(moves, crates, part1=True)
        q2 = stacking(moves, crates, part1=False)

        print(q1)
        print(q2)
