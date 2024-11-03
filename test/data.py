import numpy as np
def aver(*args):
    return sum(args)/len(args)
def std(*args):
    return (sum([(i-aver(*args))**2 for i in args])/len(args))**0.5 # 标准差
def sem(*args):
    return std(*args)/(len(args)-1)**0.5

from scipy.stats import sem

# 假设我们有一些测量值
measurements = np.array([0.788,0.744,0.827,0.840,0.780])

# 计算平均值
mean_value = np.mean(measurements)

# 计算标准误差（Standard Error，即不确定度的一种）
standard_error = sem(measurements)
TP=0;
if len(measurements)==4:
    TP=1.20
elif len(measurements)==3:
    TP=1.32
elif len(measurements)==2:
    TP=1.84
elif len(measurements)==5:
    TP=1.14
print(f"平均值: {mean_value}")
print(f"标准误差（不确定度）: {TP*standard_error}")
print("u=",TP*sem(measurements))