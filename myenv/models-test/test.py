# n_students_and_subjects = input()
# n_students, subjects = [int(i) for i in n_students_and_subjects.split(" ")]
# all_scores = []

# for _ in range(subjects):
#     scores = input()
#     scores_int = [int(_) for _ in scores.split(" ")]
#     all_scores.append(scores_int)
    
# scores_per_student = zip(*all_scores)

# print(scores_per_student)
    



    
# # test = ['1', '2']
# # test_int = [int(x) for x in test]
# # print(test_int)

# # temp = n_students_and_subjects.split()
# # n_students = int(temp[0])
# # subjects = int(temp[1])

from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    data = input().split()
    combs = list(combinations(data, int(input())))
    occur = [x for x in combs if "a" in x]
    
    print(f"{len(occur)/len(combs):.3f}")