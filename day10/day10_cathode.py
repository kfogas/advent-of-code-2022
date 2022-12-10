import re

cycle = 0
reg_value = 1
part1 = 0


def inc_cycle():
    global cycle, part1
    cycle += 1
    if (cycle == 20) or ((cycle-20) % 40 == 0):
        print(f'{cycle}th cycle')
        print(f'Reg vaule: {reg_value}')
        part1 += cycle*reg_value
        print(f'Signal strength: {part1}')


if __name__ == '__main__':
    with open('input') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line == 'noop':
                inc_cycle()
            else:
                # add = int(''.join(filter(str.isdigit, line)))
                nums = re.compile(r"[+-]?\d+(?:\.\d+)?")
                add = int(nums.search(line).group(0))
                inc_cycle()
                inc_cycle()
                reg_value += add
    print(part1)
