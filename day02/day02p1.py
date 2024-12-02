# Advent of Code 2024
# Day 2, Part 1
# Compute a slightly different function over several lists 

# Given a list of integers: 
# 1. Break them into a sequence 
# 2. They are "Safe" if monotonically increasing or decreasing, AND
# 3. They are "Safe" if the absolute difference between two values is from 1-3 
# Compute the total number of "Safe" reports in the file of lines (Test should yield 2)

import math
import itertools
from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        reports = []
        lines = open(filename).read().splitlines()
        for line in lines:
            reports.append(list(map(int, line.split(" "))))
        self.reports = reports
        return
    
    def isMonotonic(self, report):
        m = True
        for i, reading in enumerate(report):
            if i < 2:
                pass
            # TODO: add exception handling for divide-by-zero
            elif ((report[i - 2] - report[i - 1]) / (report[i - 1] - report[i]) < 0):
                return False 
        return True
    
    def isGentlysloped(self, report):
        
        return g

    def safety(self):
        sum = 0
        for r in self.reports:
            if self.monotonic(r) and self.gentlysloped(r):
                sum += 1
            else:
                pass
        return sum 


def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2024\\day02\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2024\\day02\\input.txt")  

    print("Test similarity is {}".format(t.safety()))
    print("Real similarity is {}".format(p.safety()))

if __name__ == "__main__":
    main()
