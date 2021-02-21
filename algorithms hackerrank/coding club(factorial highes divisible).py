def findPowerPrime(fact, p): 
    res = 0
    while fact:      
        res += fact // p 
        fact //= p 
  
    return res
def findPowerComposite(fact, n):  
    res = math.inf 
    for i in range(2, int(n**0.5) + 1): 
        count = 0
        if not n % i: 
            count += 1
            n = n // i 
  
        if count:  
            curr_pow = findPowerPrime(fact, i) // count 
            res = min(res, curr_pow) 
    if n >= 2: 
        curr_pow = findPowerPrime(fact, n) 
        res = min(res, curr_pow) 
  
    return res
