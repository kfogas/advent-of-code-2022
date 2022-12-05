actual = 0
max = 0

top3 = [0, 0, 0]

if __name__ == '__main__':
    with open("input", "r") as f:
        for line in f:
            if line == '\n':
                if max < actual:
                    max = actual

                if min(top3) < actual:
                    top3[top3.index(min(top3))] = actual

                actual = 0

            else:
                actual += int(line)

    print(max)
    print(sum(top3))
