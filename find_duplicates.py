def findDuplicate(arr):
    temp = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if(temp[arr[i]-1]!=0):
            return arr[i]
        else:
            temp[arr[i]-1] = arr[i]

print(findDuplicate([1,3,4,2,4]))



"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = nums
        slow = arr[0]
        fast = arr[0]
        flag = True
        if(flag):
            slow = arr[slow]
            fast = arr[arr[fast]]
            flag = False
        while slow!=fast:
            slow = arr[slow]
            fast = arr[arr[fast]]

        fast = arr[0]
        while(slow!=fast):
            slow = arr[slow]
            fast = arr[fast]
        return slow
"""
