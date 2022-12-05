def letter_values(letter: str) -> int:
    if letter.isupper():
        value = ord(letter)-38
    if letter.islower():
        value = ord(letter)-96
    return value


def part1(line):
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    for letter in secondpart:
        if letter in firstpart:
            value = letter_values(letter)
            break
    return value


def part2(lines):
    line1, line2, line3 = lines

    for letter in line1:
        if letter in line2:
            if letter in line3:
                value = letter_values(letter)
    return value


if __name__ == '__main__':
    points = 0
    points2 = 0
    lines2 = [0, 0, 0]
    i = 0

    with open('input_d3', 'r') as f:
        data = f.read()
        lines = data.split('\n')
        for line in lines:
            points += part1(line)

        while i < len(lines):
            lines2 = lines[i:i+3]
            points2 += part2(lines2)
            i += 3

    print(points)
    print(points2)
