#!/usr/bin/python
import re

NUM_CUBES = [12, 13, 14]

class Game:
    def __init__(self, s, red, green, blue):
        self._draws = []
        self._red = red
        self._green = green
        self._blue = blue

        draws = re.sub(r'Game \d+: +', '', s).split(';')
        for d in draws:
            red = None
            green = None
            blue = None

            colors = d.split(',')
            for color in colors:
                color = color.strip()
                m = re.match(r'(\d+) +(red|green|blue)', color)
                if m.group(2) == 'red':
                    red = m.group(1)
                elif m.group(2) == 'green':
                    green = m.group(1)
                elif m.group(2) == 'blue':
                    blue = m.group(1)
            self._draws.append(draw(red, green, blue))

    def possible(self):
        for draw in self._draws:
            if draw[0] > self._red:
                return False
            if draw[1] > self._green:
                return False
            if draw[2] > self._blue:
                return False

        return True

    def minimum(self):
        red = 0
        green = 0
        blue = 0

        for draw in self._draws:
            if draw[0] > red:
                red = draw[0]

            if draw[1] > green:
                green = draw[1]

            if draw[2] > blue:
                blue = draw[2]

        return [red, green, blue]

    def power(self):
        m = self.minimum()
        total = 1
        for x in m:
            if x != 0:
                total = total * x

        return total


def draw(red, green, blue):
    _red = 0
    _green = 0
    _blue = 0

    if red is not None:
        _red = int(red)

    if green is not None:
        _green = int(green)

    if blue is not None:
        _blue = int(blue)

    return [_red, _green, _blue]


def read_games(file):
    games = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            games.append(Game(line, *NUM_CUBES))
            line = f.readline()

    return games


def sum_possible_games(games):
    total = 0
    for i, game in enumerate(games):
        if game.possible():
            total = total + i + 1

    return total


def sum_power_games(games):
    total = 0
    for game in games:
        total = total + game.power()

    return total


games = read_games('input.txt')
print('possible: ', sum_possible_games(games))
print('power: ', sum_power_games(games))
