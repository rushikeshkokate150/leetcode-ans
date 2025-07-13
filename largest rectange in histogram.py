# brute force
def NSE(arr):
    st = []
    nse = [len(arr)] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        if st:
            nse[i] = st[-1]
        st.append(i)
    return nse

def PSE(arr):
    st = []
    pse = [-1] * len(arr)
    for i in range(len(arr)):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        if st:
            pse[i] = st[-1]
        st.append(i)
    return pse

heights = [2,1,5,6,2,3]
nse=NSE(heights)
pse=PSE(heights)
print(nse)
print(pse)
maxi=0
for i in range(0,len(heights)):
    maxi=max(maxi,heights[i]*(nse[i]-pse[i]-1))
    print((nse[i]-pse[i]-1))
print(maxi)

# optimal sol

stack1=[]
maxia=0
for i in range(0,len(heights)):
    while(len(stack1)!=0 and heights[stack1[-1]]>heights[i]):
        element=stack1[-1]
        stack1.pop()
        nse1=i
        pse1=-1 if len(stack1)==0 else stack1[-1]
        maxia=max(maxia,heights[element]*(nse1-pse1-1))
    stack1.append(i)
while(len(stack1)!=0):
    nse1=len(heights)
    element=stack1[-1]
    stack1.pop()
    pse1=-1 if len(stack1)==0 else stack1[-1]
    maxia=max(maxia,heights[element]*(nse1-pse1-1))
print(maxia)
        
        