
def comparism(a, b,c):
    if a>b and a>c:
        return ('a is the biggest')
    elif b>a and b>c:
        return ('b is the biggest')
    elif c>a and c>b:
        return ('c is the biggest')
    else:
        return('no single biggest number')




print(comparism(a=94,b=17,c=67))