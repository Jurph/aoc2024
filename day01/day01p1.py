# Advent of Code 2024
# Day 1, Part 1
# Compute a function over several lists 

# Given a list with pairs of integers: 
# 1. Break them into two lists 
# 2. Sort both lists ascending  
# 3. The distance between them (absolute value) should be added to a sum 


from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        integers = []
        strings = [] 
        pairs = []
        lines = open(filename).read().splitlines()
        for line in lines:
            strings.append(line)
            pairs.append(line.split())
            try:
                integers.append(int(line))
            except(ValueError):
                integers.append(int(0))
        self.strings = strings
        self.integers = integers
        return
    
