len=int(input("马路长度"))
l=[x for x in range(0,len+1)]
x= input("区域数量")
x=int(x)
for i in range(0,x):
    a=input("开始位置")
    b=input("结束位置")
    a=int(a)
    b=int(b)
    for j in l:
        if j>=a and j<=b:
            l[j]=-1
num=0
for i in l:
    if i!=-1:
        num+=1
print(num)