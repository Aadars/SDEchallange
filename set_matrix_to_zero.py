def setZeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rows = [-1 for i in range(n)]
    cols = [-1 for i in range(m)]
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                rows[i] = 0
                cols[j] = 0

    for i in range(n):
        for j in range(m):
            if(rows[i]==0 or cols[j]==0):
                matrix[i][j] = 0
    return matrix
    
t = int(input())
while t:
    n,m =[int(i) for i in input().split()]
    matrix =[]
    for i in range(n):
        l = [int(i) for i in input().split()]
        matrix.append(l)
    res = setZeros(matrix)
    for i in range(n):
        for j in range(m):
            print(matrix[i][j],end=" ") 
        print()
    t-=1
            

