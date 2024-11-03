s="八百标兵奔北坡，北坡八百炮兵炮。标兵怕碰炮兵炮，炮兵怕把标兵碰。"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
l=[];
for i in d:
    l.append((i,d[i]));
l.sort(key=lambda x:x[1],reverse=True)
print(l)

