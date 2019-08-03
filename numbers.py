import sys

def get_counts(l):
    count = [0,0,0,0,0,0,0,0,0,0]
    for word in l:
        count[len(word)] += 1
    return count