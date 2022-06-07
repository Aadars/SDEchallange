def merge(arr1,arr2,n,m):
    back = len(arr1)-1 - len(arr2)
    for i in range(len(arr1)-1,back,-1):
        arr1.pop(i)
    n = len(arr1)
    m = len(arr2)
    arr3 = [0 for i in range(n+m)]
    k = 0
    i = 0
    j = 0
    while(i<n and j<m):
        if(arr1[i]<arr2[j]):
            arr3[k] = arr1[i]
            k+=1
            i+=1
        else:
            arr3[k] = arr2[j]
            k+=1
            j+=1

    while(i<n):
        arr3[k]=arr1[i]
        k+=1
        i+=1
    while(j<m):
        arr3[k] = arr2[j]
        k+=1
        j+=1
    return arr3

print(merge([3,6,9,0,0],[4,10],4,2))
