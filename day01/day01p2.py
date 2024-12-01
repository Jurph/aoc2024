# Advent of Code 2024
# Day 1, Part 2
# Compute a slightly different function over several lists 

# Given a list with pairs of integers: 
# 1. Break them into two lists 
# 2. Multiply each unique digit from the left list by the number of times it occurs on the right list 
# 3. The sum of those products is the "similarity"

import math
import itertools
from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        pairs = []
        leftintegers = []
        rightintegers = []
        lines = open(filename).read().splitlines()
        for line in lines:
            pairs.append(line.split("   "))
        leftintegers, rightintegers = list(zip(*pairs))
        leftintegers = list(map(int, leftintegers))
        rightintegers = list(map(int, rightintegers))
        self.leftintegers = leftintegers
        self.rightintegers = rightintegers
        return
    
    # "span" is residual from part 1
    def span(self):
        sum = 0
        lefty = sorted(self.leftintegers)
        righty = sorted(self.rightintegers)
        for (l, r) in zip(lefty, righty):
            sum += abs(l-r)
        return sum
    
    # "similarity" solves part 2
    def similarity(self):
        similarity = 0
        for l in self.leftintegers:
            similarity += l * self.rightintegers.count(l)
        return similarity


def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2024\\day01\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2024\\day01\\input.txt")  

    print("Test similarity is {}".format(t.similarity()))
    print("Real similarity is {}".format(p.similarity()))

if __name__ == "__main__":
    main()
