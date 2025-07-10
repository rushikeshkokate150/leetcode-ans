# sice it using the arry to store the profit weight  ratio so it space complexcity is O(n)
# time complexcity is O(n)
total=0
profit=[280,100,120,120]
wight=[40,10,20,24]
w=60
profitbyweight=[]
for i  in range(len(wight)):
    profitbyweight.append(round(profit[i]/wight[i],3))
print(profitbyweight)
while w>0:
    maximum=max(profitbyweight)
    i=profitbyweight.index(maximum)
    if wight[i]<w:
        w-=wight[i]
        total+=profit[i]
    else:
        total+=w*profitbyweight[i]
        w-=wight[i]
    profitbyweight[i]=-1
print(total)