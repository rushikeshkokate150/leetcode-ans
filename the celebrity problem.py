mat=[[0,1,1,0],[0,0,0,0],[0,1,0,0],[1,1,0,0]]
# optimal solution
top=0
down=len(mat)-1
while(top<down):
    if(mat[top][down]==1):
        top+=1
    elif mat[down][top]==1:
        down-=1
    else:
        top+=1
        down-=1
if top>down:
    print(-1)
    print("Due to top>down")
for i in range(len(mat)):
    if i==top:
        continue
    if mat[top][i]==0 and mat[i][top]==1:
        continue
    else:
        print(-1)
        break
print(top)