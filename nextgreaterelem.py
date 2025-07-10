arr=[6,0,8,1,3]
ans=[0]*len(arr)
for r in range(0,len(arr)-1):
    maxm=max(arr[r+1:len(arr)])
    if arr[r]>maxm:
        ans[r]=-1
    else:
        ans[r]=maxm
ans[-1]=-1
print(ans)