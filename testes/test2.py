""" def subsc_candidates():
    N = int(input())
    candidates = []

    for _ in range(N):
        nome, A, B, C = input().split()
        total_points = int(A) + int(B) + int(C)
        candidates.append((nome, total_points))
        
    return candidates


def evaluate_candidates(list):
    list.sort(key=lambda x: (-x[1], x[0].title()))

    for candidate in list:
        print(candidate[0])  
    

candidates_list = subsc_candidates()
print("\n")
evaluate_candidates(candidates_list) """

import random

a = [1, 2, 3, 4,  5]
b = random.choice(a)
print(b, b.__index__())
a.remove(b.__index__())
print(a)