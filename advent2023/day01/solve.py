#!/usr/bin/python
import re

RE = re.compile(r'(?=(1|one|2|two|3|three|4|four|5|five|6|six|7|seven|8|eight|9|nine))')

def extract_digits(s):
    values = RE.findall(s)
    for value in values:
        if value == 'one':
            yield 1
        elif value == 'two':
            yield 2
        elif value == 'three':
            yield 3
        elif value == 'four':
            yield 4
        elif value == 'five':
            yield 5
        elif value == 'six':
            yield 6
        elif value == 'seven':
            yield 7
        elif value == 'eight':
            yield 8
        elif value == 'nine':
            yield 9
        else:
            yield int(value)

def find_calibration_value(s):
    first = None
    last = None

    for d in extract_digits(s):
        if not first:
            first = d
        else:
            last = d

    if last is None:
        last = first

    try:
        value = 10 * first + last
    except Exception as e:
        print(s)
        raise e

    return value

def read_calibration_values(file):
    values = []

    with open(file, 'r') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            values.append(find_calibration_value(line))
            line = f.readline()

    return values


values = read_calibration_values('input.txt')
print(sum(values))
