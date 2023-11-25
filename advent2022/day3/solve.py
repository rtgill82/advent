#!/usr/bin/python

def item_value(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96

class Group:
    GROUPS = []

    def __init__(self):
        Group.GROUPS.append(self)
        self.count = 0
        self.packs = []

    def add_pack(self, pack):
        self.count += 1
        self.packs.append(pack)
        if self.count == 3:
            return Group()
        else:
            return self

    def count(self):
        return self.count

    def find_badge(self):
        return (set(self.packs[0]) & set(self.packs[1]) & set(self.packs[2])).pop()

    @classmethod
    def calculate_group_badges(cls):
        if cls.GROUPS[-1].count == 0:
            cls.GROUPS.pop()

        total = 0
        for group in cls.GROUPS:
            total += item_value(group.find_badge())
        return total

total = 0
with open('input.txt') as file:
    line = file.readline()
    group = Group()
    while line:
        pack = [*(line.strip())]
        group = group.add_pack(pack)
        mid = int(len(pack)/2)
        item = (set(pack[:mid]) & set(pack[mid:])).pop()
        total += item_value(item)
        line = file.readline()

print("The sum of item priorites appearing in both compartments is:", total)
print("The sum of all group badges is:", Group.calculate_group_badges())
