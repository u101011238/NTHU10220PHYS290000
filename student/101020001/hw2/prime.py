def prime(j):
    p=[2]
    n=3
    while n<=j :
        i=1
        while i<=n**(0.5) :
            if n%(i+1)==0 :
                i=i+1
                break
            elif i==int(n**(0.5)) :
                p.append(n)
            i=i+1
        n=n+1
    print p
prime(10000)

