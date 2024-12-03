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
        if sorted(report) == report:
            return True
        elif sorted(report, reverse = True) == report:
            return True
        else:            
            return False
    
    def isGentlysloped(self, report):
        for index, reading in enumerate(report):
            if index == 0:
                pass
            elif abs(reading - report[index - 1]) > 3:
                return False
            elif abs(reading - report[index - 1]) < 1:
                return False
            else:
                pass
        return True

    def safety(self):
        sum = 0
        for r in self.reports:
            if self.isMonotonic(r) and self.isGentlysloped(r):
                sum += 1
                # print("Found SAFE report: {}".format(r))
            else:
                pass
                # print("Found UNSAFE report: {}".format(r))
        return sum 


def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2024\\day02\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2024\\day02\\input.txt")  

    print("Test safety should be 2: is {}".format(t.safety()))
    print("Real safety is: {}".format(p.safety()))

if __name__ == "__main__":
    main()
