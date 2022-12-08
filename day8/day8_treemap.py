treemap = []


def detect_higher(current, row, pos):
    if current > max(row[:pos]):
        return True
    if current > max(row[pos+1:]):
        return True
    return False


def count_visibility():
    count = 0
    for i in range(1, len(treemap)-1):
        for j in range(1, len(treemap)-1):

            # Check row
            if detect_higher(treemap[i][j], treemap[i], j):
                count += 1
                continue

            # Check column
            column = []
            for row in treemap:
                column.append(row[j])
            if detect_higher(treemap[i][j], column, i):
                count += 1
                continue
    count += (len(treemap)*4)-4

    return count


def higher_dist(current, row, pos):
    a = row[:pos]
    a.reverse()
    b = row[pos+1:]
    a_count = 0
    b_count = 0

    for i in range(len(a)):
        a_count += 1
        if current <= a[i]:
            break

    for i in range(len(b)):
        b_count += 1
        if current <= b[i]:
            break

    return a_count * b_count


def scenic_score():
    scenic = 0
    for i in range(1, len(treemap)-1):
        for j in range(1, len(treemap)-1):

            # Check row
            a = higher_dist(treemap[i][j], treemap[i], j)

            # Check column
            column = []
            for row in treemap:
                column.append(row[j])

            b = higher_dist(treemap[i][j], column, i)

            temp_scenic = a * b
            if temp_scenic > scenic:
                scenic = temp_scenic
    return scenic


if __name__ == '__main__':
    with open('input') as f:
        lines = f.read().splitlines()
        for line in lines:
            treemap.append(list(map(int, [*line])))
        print(count_visibility())
        print(scenic_score())
