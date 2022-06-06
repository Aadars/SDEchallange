"""def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    flag = False
    for i in range(n-1,0,-1):
        if(permutation[i]<permutation[i-1]):
            pass
        else:
            flag = True
            break
    if(flag):     
        for i in range(n-1):
            if(permutation[i]<permutation[i+1]):
                break
        if(i>=0):
            for j in range(n-1,-1,-1):
                if(permutation[j]>permutation[i]):
                    break
            permutation[i],permutation[j]=permutation[j],permutation[i]
        print(i,j,permutation)
        i = i+1
        j = n-1
        while(i<j):
            permutation[i],permutation[j]=permutation[j],permutation[i]
            i+=1
            j-=1
        return permutation
    else:
        return permutation[::-1]
print(nextPermutation([1,2,3], 3))
"""
def reverse(nums,start):
    start = start
    end = len(nums)-1
    while start<=end:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1
    return nums 
def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    ind1 = 0
    ind2 = 0
    flag = 0
    for i in range(len(permutation)-1):
        if(permutation[i]>=permutation[i+1]):
            pass
        else:
            flag = 1
            break
    if(flag==0):
        permutation.sort()
    else:
        for i in range(len(permutation)-1,0,-1):
            if(permutation[i-1]<permutation[i]):
                ind1 = i-1
                break
        for i in range(len(permutation)-1,-1,-1):
            if(permutation[ind1]<permutation[i]):
                permutation[ind1],permutation[i] = permutation[i],permutation[ind1]
                ind2 = i
                break
        reverse(permutation,ind1+1)
    return permutation
                
print(nextPermutation([1,2,3], 3))
        
