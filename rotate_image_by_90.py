def rotate(matrix):
    arr = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        l = [0]*m
        arr.append(l)
    for j in range(m):
        for i in range(n):
            arr[j][i] = matrix[i][j]
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    matrix = arr
    return matrix
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    
