import re


def pair_check(elf1, elf2) -> bool:
    return True if ((elf1[0] <= elf2[0]) and (elf1[1] >= elf2[1])) or ((elf2[0] <= elf1[0]) and (elf2[1] >= elf1[1])) else False


def overlap_check(elf1, elf2) -> bool:
    if (elf1[1] >= elf2[0]) and (elf2[1] >= elf1[0]):
        return True
    if (elf2[1] >= elf1[0]) and (elf1[1] >= elf2[0]):
        return True

    return False


if __name__ == '__main__':

    with open('input_d4', 'r') as f:
        elf1 = []
        efl2 = []
        count = 0
        count_overlap = 0
        data = f.read()
        lines = data.split('\n')
        for line in lines:
            values = (list(map(int, re.split(',|-', line))))
            elf1 = values[0:2:]
            elf2 = values[2:4:]

            if pair_check(elf1, elf2):
                count += 1

            if overlap_check(elf1, elf2):
                count_overlap += 1

    print(count)
    print(count_overlap)
