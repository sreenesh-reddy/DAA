def kn(p,w,n,W):
    ind=list(range(n)) 
    ratio =[p[i]/w[i] for i in ind]
    ind.sort(key=lambda i:ratio[i],reverse=True)
    max=0
    fractions=[0]*n
    for i in ind:
        if(w[i]<=W):
            fractions[i]=1
            max +=p[i]
            W -=w[i]
        else:
            fractions[i]=W/w[i]
            max+=p[i]*W/w[i]
            break
    return max,fractions
profits=list(map(int,input('enter profits').split()))
weights=list(map(int,input('enter weights').split()))
no=len(profits)
capacity=int(input('enter capcity'))
max,fractions=kn(profits,weights,no,capacity)
print('max profit',max)
print('fraction',fractions)