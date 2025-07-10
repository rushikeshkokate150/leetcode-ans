def b2d(n):
    l=len(n)-1
    num=0
    for i in range(len(n)):
        num+=(int(n[i])*(2**l))
        l-=1
    return num
ans=b2d("100111")
print(ans)
