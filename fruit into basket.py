arr=[3,3,3,1,2,1,1,2,3,3,4]
basket=2
b={}
count=0
l=0
ans=0
for r in range(len(arr)):
    if arr[r] not in b:
        b[arr[r]]=1
    else:
        b[arr[r]]+=1
    while len(b)>2:
        b[arr[l]]-=1
        if b[arr[l]] == 0:
            del b[arr[l]]
        l+=1
    ans=max(ans,(r-l)+1)
print(ans)
        