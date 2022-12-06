def match_point(hands):
    gamepoint = 0
    if hands[1] == 'X':
        handpoint =  1
        if hands[0] == 'A':
            gamepoint = 3
        elif hands[0] == 'C':
            gamepoint = 6

    elif hands[1] == 'Y':
        handpoint = 2
        if hands[0] == 'B':
            gamepoint = 3
        if hands[0] == 'A':
            gamepoint = 6

    elif hands[1] == 'Z':
        handpoint = 3
        if hands[0] == 'C':
            gamepoint = 3
        if hands[0] == 'B':
            gamepoint = 6

    return  handpoint + gamepoint

def switchhand(hands):
    if hands[0] == 'A':
        if hands[1] == 'X':
            ret = 'Z'
        elif hands[1] == 'Y':
            ret = 'X'
        elif hands[1] == 'Z':
            ret = 'Y'

    if hands[0] == 'B':
        if hands[1] == 'X':
            ret = 'X'
        elif hands[1] == 'Y':
            ret = 'Y'
        elif hands[1] == 'Z':
            ret = 'Z'

    if hands[0] == 'C':
        if hands[1] == 'X':
            ret = 'Y'
        elif hands[1] == 'Y':
            ret = 'Z'
        elif hands[1] == 'Z':
            ret = 'X'
    
    return [hands[0],ret]

def super_point_calculator(games):
    points = 0
    points2 = 0

    for game in games:
        hands = game.split(' ')

        p2hands = switchhand(hands)

        points += match_point(hands)
        
        points2 += match_point(p2hands)

    return points2


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
        games = data.split('\n')
        print(super_point_calculator(games))
