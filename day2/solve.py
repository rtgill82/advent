#!/usr/bin/python

def find_play(game):
    match game[0]:
        case 'A':
            match game[1]:
                case 'X':
                    return 'C'
                case 'Y':
                    return 'A'
                case 'Z':
                    return 'B'
        case 'B':
            match game[1]:
                case 'X':
                    return 'A'
                case 'Y':
                    return 'B'
                case 'Z':
                    return 'C'
        case 'C':
            match game[1]:
                case 'X':
                    return 'B'
                case 'Y':
                    return 'C'
                case 'Z':
                    return 'A'


def match_score(game):
    total = score = play_score(game[1])
    match game[0]:
        case 'A':
            match score:
                case 1:
                    total += 3
                case 2:
                    total += 6
        case 'B':
            match score:
                case 2:
                    total += 3
                case 3:
                    total += 6
        case 'C':
            match score:
                case 1:
                    total += 6
                case 3:
                    total += 3

    return total

def play_score(play):
    match play:
        case 'A'|'X':
            return 1
        case 'B'|'Y':
            return 2
        case 'C'|'Z':
            return 3
        case _:
            raise 'invalid play'

score1 = 0
score2 = 0
with open('input.txt') as file:
    line = file.readline()
    while line:
        game = line.strip().split(' ')
        line = file.readline()
        score1 += match_score(game)
        game[1] = find_play(game)
        score2 += match_score(game)



print("Your score according to what should be played is:", score1)
print("Your score according to suggested strategy is:", score2)
