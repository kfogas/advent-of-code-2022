import re

cycle = 0
reg_value = 1
part1 = 0
sprite = ''
sprite_loc = range(3)


def inc_cycle():
    global cycle, part1, sprite
    if (cycle == 20) or ((cycle-20) % 40 == 0):
        # print(f'{cycle}th cycle')
        # print(f'Reg vaule: {reg_value}')
        part1 += cycle*reg_value
        # print(f'Signal strength: {part1}')
    sprite_loc = range(reg_value-1, reg_value+2)
    if cycle in sprite_loc:
        sprite += '#'
    else:
        sprite += '.'
    cycle += 1
    if cycle == 40:
        cycle = 0


def split_to_lines(right, splitat):
    templines = []
    # right = sprite
    while len(right) >= splitat:
        left, right = right[:splitat], right[splitat:]
        templines.append(left)
    return templines


if __name__ == '__main__':
    with open('input') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line == 'noop':
                inc_cycle()
            else:
                nums = re.compile(r"[-]?\d+")
                add = int(nums.search(line).group(0))
                inc_cycle()
                inc_cycle()
                reg_value += add
    print('Part 1:', part1)
    print('Part 2:')
    print(*split_to_lines(sprite, 40), sep='\n')
