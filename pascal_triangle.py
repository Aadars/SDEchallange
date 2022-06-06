def printPascal(n):
    # Write your code here.
    # Return a list of lists.
    arr = []
    for i in range(n):
        l = []
        for j in range(i+1):
            if(j==0 or i==j):
                l.append(1)
            else:
                rs = arr[i-1][j-1] + arr[i-1][j]
                l.append(rs)
        arr.append(l)
    return arr

print(printPascal(5))
            
            
