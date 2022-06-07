from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    arr = []
    for i in intervals:
        arr.append([i.start,i.end])
    arr.sort()
        
    ans = []
    if(len(arr)==1):
        anss = []
        a = Solution(arr[0][0], arr[0][1])
        anss.append(a)
        return anss
    else:
        start = arr[0][0]
        end = arr[0][1]
        for i in range(1,len(arr)):
            if(arr[i][0]<=end):
                end = max(end,arr[i][1])
            else:
                ans.append([start,end])
                start = arr[i][0]
                end = arr[i][1]
            
        if(len(ans) ==0):
            ans.append([start,end])
        elif(ans[-1][0]!=start and ans[-1][1]!=end):
            ans.append([start,end])
    anss =[] 
    for i in range(len(ans)):
        a = Solution(ans[i][0], ans[i][1])
        anss.append(a)
    return anss
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
  

                
