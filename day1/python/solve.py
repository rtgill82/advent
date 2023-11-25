#!/usr/bin/python
from functools import reduce
from pathlib import Path

DATA = Path(__file__).parent.absolute().joinpath('../data/input.txt')

class FuelCalc:
    def __init__(self, datafile):
        self._data = self._read_data(datafile)
        self._required_fuel = None

    def required_fuel(self):
        self._required_fuel = self._required_fuel or self._sum_fuel()
        return self._required_fuel

    def _read_data(self, datafile):
        lines = []
        with open(datafile, 'r') as file:
            for line in file:
                lines.append(int(line.rstrip()))
        return lines

    def _calc_fuel(self, mass):
        return self._calc_fuel_r(mass, 0)

    def _calc_fuel_r(self, mass, total):
        mass = mass // 3 - 2
        if mass <= 0: return total
        return self._calc_fuel_r(mass, total + mass)

    def _sum_fuel(self):
        fn = lambda sum, mass: sum + self._calc_fuel(mass)
        return reduce(fn, self._data, 0)

calc = FuelCalc(DATA)
print(calc.required_fuel())
