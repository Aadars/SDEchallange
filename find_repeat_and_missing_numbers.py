arr = [3,1,2,5,3]
d = dict()
for i in range(1,len(arr)+1):
    d[i] = 0
for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]]+=1
    else:
        d[arr[i]]=0
for i in range(1,len(arr)+1):
    if(d[i]==0):
        miss = i
    if(d[i]>1):
        repeat = i
print(miss,repeat)
