# get a integer value
# 5
#the pattern should be:
# 1 * * * * 5 4 3 2 1 
# 2 1 * * * 4 3 2 1 * 
# 3 2 1 * * 3 2 1 * * 
# 4 3 2 1 * 2 1 * * * 
# 5 4 3 2 1 1 * * * * 
# * * * * 1 5 4 3 2 1 
# * * * 2 1 * 4 3 2 1 
# * * 3 2 1 * * 3 2 1 
# * 4 3 2 1 * * * 2 1 
# 5 4 3 2 1 * * * * 1

# 6
# 1 * * * * * 6 5 4 3 2 1 
# 2 1 * * * * 5 4 3 2 1 * 
# 3 2 1 * * * 4 3 2 1 * * 
# 4 3 2 1 * * 3 2 1 * * * 
# 5 4 3 2 1 * 2 1 * * * * 
# 6 5 4 3 2 1 1 * * * * * 
# * * * * * 1 6 5 4 3 2 1 
# * * * * 2 1 * 5 4 3 2 1 
# * * * 3 2 1 * * 4 3 2 1 
# * * 4 3 2 1 * * * 3 2 1 
# * 5 4 3 2 1 * * * * 2 1 
# 6 5 4 3 2 1 * * * * * 1


n=int(input());c=1;m=n-1;l=0;t=n;s=n-1;st=1;
for i in range(n):
    for k in range(st,0,-1):
        print(k,end=" ")
    for j in range(s):
        print('*',end=" ")
    for j in range(t,0,-1):
        print(j,end=" ")
    for j in range(l):
        print("*",end=" ")
    print("\r")    
    st+=1;
    s-=1;
    t-=1;
    l+=1
st=n-1;
c=1;
s=0;
f=n;
for i in range(n):
    for j in range(st,0,-1):
        print("*",end=" ");
    for j in range(c,0,-1):
        print(j,end=" ");
    for j in range(s):
        print("*",end=" ")
    for j in range(f,0,-1):
        print(j,end=" ")
    print("\r");
    st-=1;
    c+=1;
    s+=1;
    f-=1;