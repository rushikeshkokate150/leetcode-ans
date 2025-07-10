arr=[2,10,12,1,11]
n=len(arr)
st=[]
ans=[0]*n
for r in range((2*n)-1,-1,-1):
    ind=r%n
    while(len(st)!=0 and st[-1]<=arr[ind]):
        st.pop()
    if r<n:
        if len(st)==0:
            ans[r]=-1
        else:
            ans[r]=st[-1]
    st.append(arr[ind])
print(ans)