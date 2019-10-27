import random
N = 50000#試行回数
Data = []
for _ in range(N):
    I = [i for i in range(1,53)]#トランプ
    #I内のiをi=13a+bと書くとき,aがトランプの絵柄,bが数字に対応
    for i in range(1,12):
        if i == 11:#残り2枚の段階までゲームが終了しなかった場合
            Data.append(20)
            break
        S = set([])#抽出されたトランプの数字
        for __ in range(5):#ランダムに5枚カードを引く
            a = random.sample(I,1)[0]
            I.remove(a)
            S.add(a%13)#13で割った余り
        if len(S) < 5:
            Data.append(i)
            break
average = sum(Data)/N
err_data = [(Data[i]-average)**2 for i in range(N)]
error = ((sum(err_data)/N)**0.5)/(N**0.5)
print("Average:"+str(average))
print("Error:"+str(error))
