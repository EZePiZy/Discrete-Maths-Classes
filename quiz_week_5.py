def rod_cut(n,p,memo = None):
    if memo is None:
        memo = { 0 : 0,
                 1 : p[1]
                }
    
    if n not in memo: 
        bestprice = 0
        for i in range(1, n+1):
            curprice = p[i] + rod_cut(n-i, p, memo)
            if curprice > bestprice:
                bestprice = curprice
        
        memo[n] = bestprice
    return memo[n]


p = [0, 2, 7, 12, 15, 18, 19, 23, 25, 26, 31]
#p = [0, 1, 5, 8, 9 ,10, 17, 17, 20]
# print(rod_cut(10,p))


def rod_cut_price(n,p,memo=None):
    C = 0
    if memo is None:
        memo = {0: (0, []), 
                1: (p[1], [1])
                }

    if n not in memo:
        bestprice = 0 
        bestcuts = None
        for i in range(1, n+1):
            price, cuts = rod_cut_price(n-i, p, memo)
            price += (p[i] - C)
            if price > bestprice:
                bestprice = price 
                bestcuts = ([i] + cuts) 
                if bestcuts == [10]:
                    bestprice += C
        memo[n] = (bestprice, bestcuts)
    return memo[n] 


print(rod_cut_price(10,p))

