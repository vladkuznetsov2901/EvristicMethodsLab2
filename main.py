import random
from matrix_functions import *
import sys

N = int(input("Enter cnt of rows: "))
M = int(input("Enter cnt of columns: "))
T = [[0] * M for _ in range(N)]

a = int(input("Enter value from: "))
b = int(input("Enter value to: "))

sum_columns = []

for i in range(M):
    sum_columns.append(0)

for i in range(N):
    for j in range(M):
        T[i][j] = random.randint(a, b)

for row in T:
    print(row, "Сумма: ", sum(row))

sorted_T = sorted(T, key=lambda x: sum(x), reverse=True)

print("\nSorted by row sum:")
for row in sorted_T:
    print(row, "Сумма: ", sum(row))

final_matrix = [[]]
min_i = 0
min_j = 0
min_el = sorted_T[0][0]

for j in range(M):
    if sorted_T[0][j] < min_el:
        min_el = sorted_T[0][j]
        min_j = j

sum_columns[min_j] += min_el

print("\n")
print(sum_columns)

min_el = 999

for i in range(1, N):
    min_el = 999
    for j in range(M):
        if sum_columns[j] == 0 and sorted_T[i][j] < min_el:
            min_el = sorted_T[i][j]
            min_j = j
    if 0 not in sum_columns:
        break
    sum_columns[min_j] += min_el

print("\n")

print(sum_columns)
min_j = 0
for i in range(len(sum_columns), N):
    min_el = 999
    for j in range(M):
        min_j = find_min_index(sum_columns)
        min_el = sorted_T[i][min_j]
    print(min_j)
    sum_columns[min_j] += min_el
    print(sum_columns)

print("\n")

print(sum_columns)

print("Max:", max(sum_columns))
