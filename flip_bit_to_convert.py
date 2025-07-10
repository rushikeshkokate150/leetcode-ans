start=10
goal=7
ans=start^goal
print(ans)
cnt=0
while ans!=0:
    print(ans%2)
    cnt+=ans%2
    ans=int(ans/2)
print(cnt)