def summ(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
t=[(1,2),(3,4),(5,6)]
t.sort(key=lambda x:x[1],reverse=1)
print(t)