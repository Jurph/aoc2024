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
        pairs = []
        leftintegers = []
        rightintegers = []
        lines = open(filename).read().splitlines()
        for line in lines:
            pairs.append(line.split())
        leftintegers, rightintegers = list(zip(*pairs))
        leftintegers = list(map(int, leftintegers))
        rightintegers = list(map(int, rightintegers))
        self.leftintegers = leftintegers
        self.rightintegers = rightintegers
        return
    
if __name__ == "__main__":
    p = Problem("test.txt")
    print(p.leftintegers, p.rightintegers)