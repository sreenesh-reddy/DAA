def mm(i,j,a):
    if(i==j):
        return(a[i],a[j])
    elif(j-i==1):
        if(a[i]>a[j]):
            return(a[j],a[i])
        else:
            return(a[i],a[j])
    else:
        m=i+j//2
        lmin,lmax=mm(i,m,a)
        rmin,rmax=mm(m+1,j,a)
        max=0
        min=0
        if(lmax>rmax):
            max=lmax
        else:
            max=rmax
        if(lmin<rmin):
            min=lmin
        else:
            min=rmin
        return(min,max)

print('enter elmenets')
a = [int(x) if type(x)==int else x for x in input().split()]
print(a)
min,max=mm(0,len(a)-1,a)
print(min,max)


