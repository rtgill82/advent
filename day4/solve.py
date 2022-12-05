#!/usr/bin/python

def assignments(line):
    pair = []
    for assignment in line.strip().split(','):
        start, stop = list(map(int, assignment.split('-')))
        assignment = set(range(start, stop + 1))
        pair.append(assignment)

    return pair

def contained(pair):
    return pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])

def intersect(pair):
    return len(pair[0].intersection(pair[1])) != 0

subsets = 0
intersections = 0
with open('input.txt') as file:
    line = file.readline()
    while line:
        pair = assignments(line)
        if contained(pair):
            subsets += 1
        if intersect(pair):
            intersections += 1
        line = file.readline()

print("Number of assignments fully containing another:", subsets)
print("Number of assignments overlapping:", intersections)
