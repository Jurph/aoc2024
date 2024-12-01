# Advent of Code 2024
# Day 1, Part 1
# Compute a function over several lists 

# Given a list with pairs of integers: 
# 1. Break them into two lists 
# 2. Sort both lists ascending  
# 3. The distance between them (absolute value) should be added to a sum 

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
        # self.sum = self.span()
        return
    
    def span(self):
        sum = 0
        lefty = sorted(self.leftintegers)
        righty = sorted(self.rightintegers)
        for (l, r) in zip(lefty, righty):
            sum += abs(l-r)
        return sum


def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2024\\day01\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2024\\day01\\input.txt")  

    print("Test sum is {}".format(t.span()))
    print("Real sum is {}".format(p.span()))

if __name__ == "__main__":
    main()
