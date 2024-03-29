import numpy as np

# Matriz A
A = np.array( [[1, 3, 5],
               [6, 32, 1],
               [5, 3, 9] ] )
print(f"A = {A}")

# Matriz B
B = np.array( [[3, 7, 1],
               [5, 2, 7],
               [9, 8, 9]])
print(f"\n B = {B}")

# calculo final

C = np.dot(A, B)
print(f"\n A * B = {C}")