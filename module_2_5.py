def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(int(value))
    return matrix
matrix = get_matrix
result1 = get_matrix(5,2,14)
result2 = get_matrix(2,5,8)
result3 = get_matrix(2,3,10)
print(result1)
print(result2)
print(result3)