import os
import pandas as pd

os.chdir("/Users/kawaisk/Dropbox/UTap2019/3A/応用統計学") #ファイルがあるディレクトリ
data = pd.read_csv('ippan_2009zensho_z_dataset.csv', engine='python')

expend = data["L_Expenditure"] #消費支出
food = data["Food"] #食料費
housing = data["Housing"] #住居費
trans = data["Transport"] #交通・通信費
N = len(expend)

Engel = [food[i]/expend[i] for i in range(N)] #エンゲル係数
housedeg = [housing[i]/expend[i] for i in range(N)] #住居費が消費支出に占める割合
transdeg = [trans[i]/expend[i] for i in range(N)] #交通・通信費が消費支出に占める割合

#重回帰分析
a = 0;b = 0;c = 0 #X^TX = [a,b;b,c]
p = 0;q = 0 # X^Ty = [p;q]
for i in range(N):
    a += housedeg[i]**2
    b += housedeg[i]*transdeg[i]
    c += transdeg[i]**2
    p += housedeg[i]*Engel[i]
    q += transdeg[i]*Engel[i]
b_h = (p*c-b*q)/(a*c-b**2) #住居費の係数
print(b_h)
b_t = (a*q-b*p)/(a*c-b**2) #交通・通信費の係数
print(b_t)

predict = [b_h*housedeg[i]+b_t*transdeg[i] for i in range(N)] #予測値
ave = sum(Engel)/N #平均値
ave_pre = sum(predict)/N #予測値の平均値
C = 0
v = 0
V = 0

for i in range(N):
    C += (Engel[i]-ave)*(predict[i]-ave_pre) #共分散
    v += (Engel[i]-ave)**2 #元の分散
    V += (predict[i]-ave_pre)**2 #予測値の分散

R = (C*C)/(v*V) #決定係数
print(R)
