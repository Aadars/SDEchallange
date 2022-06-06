def maxSubarraySum(arr, n) :

    maxi = 0
    ans =0
    for i in range(n):
        ans+=arr[i]
        if(ans>maxi):
            maxi = ans
        if(ans<0):
            ans =0
    return maxi

    
