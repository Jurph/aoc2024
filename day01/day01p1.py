# Advent of Code 2024
# Day 1, Part 1
#  

from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        strings = [] # We don't need strings in this chapter but it's a neat feature
        integers = []
        lines = open(filename).read().splitlines()
        for line in lines:
            strings.append(line)
            try:
                integers.append(int(line))
            except(ValueError):
                integers.append(int(0))
        self.strings = strings
        self.integers = integers
        return
    
