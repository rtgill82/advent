#!/usr/bin/python

totals = []
with open('input.txt') as file:
    while True:
        calories = 0
        line = file.readline()
        while line:
            if line == '\n':
                break

            calories += int(line)
            line = file.readline()

        totals.append(calories)
        if line == '':
            break

totals.sort()
totals.reverse()
print("Highest calories of supplies carried by an elf:", totals[0])

top3 = sum(totals[0:3])
print("Total calories carried by top 3 elves:", top3)
