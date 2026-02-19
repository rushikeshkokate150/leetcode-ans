arr=[3,1,4]
ans=[]

def subsets(ind,sum):
    if ind == len(arr):
        ans.append(sum)
        return
    sum+=arr[ind]
    subsets(ind+1,sum)
    sum-=arr[ind]
    subsets(ind+1,sum)
    print("")
    
subsets(0,0)
print(ans)