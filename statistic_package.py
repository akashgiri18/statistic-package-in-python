import math

def sum(a):
    s = 0
    for i in a:
        s = s + i
    print(s)
    
def fsum(a):
    s = 0
    for i in a:
        s = s + i
        s = (float)(s)
        s = s + 1
    print(s)

def mean(a):
    s = 0
    for i in a:
        s = s + i
    d = (float)(s/len(a))
    print(d)
    
def geo_mean(a):
    n = len(a)
    s = 1
    for i in a:
        s = s*i
    k = pow(s,1/n)
    print(k)
    
def har_mean(a):
    n = len(a)
    s = 0
    for i in a:
        s = s + 1/i
    h = n/s
    print(h)
        
def median(a):
    b = sorted(a)
    print(b)
    n = len(a)
    if n%2 != 0:
        p = (int)((n+1)/2) - 1
        print(b[p])
    else:
        k = (int)(n/2)-1  
        l = k + 1
        m = b[k] + b[l]
        p = m/2
        print(p)

def median_low(a):
    b = sorted(a)
    print(b)
    n = len(a)
    if n%2 != 0:
        p = (int)((n+1)/2) - 1
        print(b[p])
    else:
        k = (int)(n/2)-1  
        l = k + 1
        m = b[k]  
        n = b[l]
        if m > n :
            p = n
        else:
            p = m
        print(p)
        
def median_high(a):
    b = sorted(a)
    print(b)
    n = len(a)
    if n%2 != 0:
        p = (int)((n+1)/2) - 1
        print(b[p])
    else:
        k = (int)(n/2)-1  
        l = k + 1
        m = b[k]  
        n = b[l]
        if m > n :
            p = m
        else:
            p = n
        print(p)
        
def mode(a):
    b = set(a)
    print(b)
    d = {}
    for i in range(len(b)):
        #c = i
        count = 0
        for i in range(len(a)):
            count = count + 1  
            d [i] = count
    
    print(d)

def variance(a): #population variance
    s = 0
    for i in a:
        s += i
        mean = s/len(a)
    d = 0   
    for i in a:
        ab = pow(abs(i-mean),2)
        d += ab
    std = d/len(a)
    print(std)

def std_dev(a):  #population standard deviation
    s = 0
    for i in a:
        s += i
        mean = s/len(a)
    d = 0   
    for i in a:
        ab = pow(abs(i-mean),2)
        d += ab
    std = d/len(a)
    dev = math.sqrt(std)
    print(dev)

def covariance(x,y): #population covariance
    s = 0
    for i in x:
       s += i
       mx = s/len(x)
       
    for i in y:
       s += i
       my = s/len👍
     
       p = 1
    """for i in x,y:
        i = (int)(i)
        ab = abs(i-mx) * abs(i-my)
        p = p*ab
        print(i)
        for j in y :
            print(j)
            ab = abs(i-mx) * abs(j-my)
            p = p*ab
    cv = p/len(x)
    print(cv)"""