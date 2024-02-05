
def f1(a, c):
    cc = 0
    for e in c:
        if e % 10 == 0:
            cc += 1
    
    return a[-1] == 'H', cc

print(f1('joheH', [1, 20, 13, 50, 6]))

def f2(a, c):
    cc = 0
    for e in c:
        if e % 2 != 0:
            cc += 1
    
    return len(a) == cc, cc

print(f2('oieu', [1,2,4,7,9,10]))

def f3(a, c):
    cc = 0
    for e in c:
        if e % 2 == 0:
            cc += 1
    
    return len(a) > 0, cc

print(f3('oie', [1,2,4,7,9,11]))

def f4(a, c):
    cc = 0
    for e in c:
        if e > len(a):
            cc += 1
    
    return a[:2] == 'gu', cc

print(f4('ugie', [1,2,4,7,9,10]))

def f5(a, c):
    cc = 0
    for e in c:
        if e >= 10:
            cc += 1
    
    return a.lower().count('h') == 2, cc

print(f5('joheH', [1, 13, 10, 50, 9]))
