#!/usr/bin/python3
def best_score(a):
    return max(a, key=a.get) if a else None
