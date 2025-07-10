arr=[4,12,5,3,1,2,5,3,1,2,4,6]
st=[]
ans=[0]*len(arr)
for i in range(len(ans)-1,-1,-1):
    if len(st)==0:
        ans[i]=-1
    elif arr[i]<st[-1]:
        ans[i]=st[-1]
    else:
        while(len(st)!=0 and st[-1]<=arr[i]):
            st.pop()
        if len(st)==0:
            ans[i]=-1
        else:
            ans[i]=st[-1]
    st.append(arr[i])
print(ans)