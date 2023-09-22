from functools import reduce

#ASSERT EN BAS

# BOUCLE SANS BOUCLE

def foo(x):
    i = 0
    v = x * x
    while i <= v :
        v = v - x
        i = i + x
    return i * v

def funct_foo(x):
    def bis(i=0, v=x*x):
        if i > v:
            return i*v
        else:
            return bis(i + x, v - x)
    return bis()

def bar(x,y):
    r=0
    for i in range(0, 10):
        r = r + x
    for j in range(r,0,-1):
        r = r - y
    return r

def funct_bar(x,y):
    r = 10*x           #on peut faire recursion x + rec jusqu'à x == 10
    def bis(j=r, r=r):
        if j == 0:
            return r
        else:
            return bis(j-1, r - y)
    return bis()

# ENSEMBLE COMME DES FONCTIONS

def car_S1(x): return x > 0

def car_S2(x):
    return (x >= 0) & (x % 2 == 0)

def car_S3(x):
    return (x==0) | (x==3) | (x==7) | (x == 9)

def car_S4(x):
    return (x >= 10) & (x <= 1000)

def car_S5(x):
    return False

def union(S, Sbis):
    return lambda x: S(x) | Sbis(x)

def inter(S, Sbis):
    return lambda x: S(x) & Sbis(x)

def ajout(x, S):
    return lambda y: (y==x) | S(y)

def ensemble(l):
    return reduce(lambda acc,x: ajout(x, acc), l, lambda x: False)
#ou avec une fonction initialisée avant le for puis qui prend ajout de chaque valeur et elle même.


# RECURSION SANS RECURSION

def fact(suite, n):
    if n == 0:
        return 1
    else:
        return n * suite(suite, n-1)
    
fact_main = lambda n: fact(fact, n)

fact_lambda = lambda n: (lambda ff,n : 1 if n ==0 else n*ff(ff, n-1))(lambda ff,n: 1 if n == 0 else n*ff(ff, n-1), n)

# PROGRAMMER DES ITERATEURS

def somme_des_carres(l):
    return reduce((lambda acc,x: acc + (x**2)), l, 0)

def maximum(l):
    return reduce(lambda acc,x: x if x >acc else acc, l, 0)

def fst(l):
    return list(map(lambda x: x[0], l))

def permute(l):
    return list(map(lambda x: 0 if x==1 else 1, l))

def compte0(l):
    return reduce(lambda acc,x: acc + 1 if x == 0 else acc, l, 0)

def pgs(v,l):
    #fonction aux qui evalue la valeur de la série actuelle et le max.
    def bis(acc,x):
        max = acc[1]
        if x == v:
            now = acc[0] + 1
        else :
            now = 0
        if now > acc[1]:
            max = now
            
        return now, max

    res = reduce(bis,l, (0, 0)) # a gauche serie actuelle a droite max
    return res[1]


#TESTS ET ASSERT        

if __name__ == "__main__":
    print("TEST FOO 4")
    print("foo(4) : ",foo(4))
    print("funct_foo(4) : ", funct_foo(4))
    assert foo(4) == funct_foo(4), "ERREUR FOO"
    print("-"*50)

    print("TEST BAR 4 3")
    print("bar(4,3) : ",bar(4,3))
    print("funct_bar(4,3) : ",funct_bar(4,3))
    assert bar(4,3) == funct_bar(4,3), "ERREUR BAR"
    print("-"*50)

    print("car_S2")
    print("car_S2(2) : ",car_S2(2))
    print("car_S2(3) : ",car_S2(3))
    assert car_S2(3) == False, "ERREUR car_S2"
    print("-"*50)

    print("car_S3")
    print("car_S3(3) : ",car_S3(3))
    assert car_S3(3) == True, "ERREUR car_S3"
    print("-"*50)

    print("car_S4")
    print("car_S4(1000) : ",car_S4(1000))
    assert car_S4(1000) == True, "ERREUR car_S4"
    print("-"*50)

    print("car_S5")
    print("union(car_S2, car_S3)(3) : ",union(car_S2, car_S3)(3))
    assert union(car_S2, car_S3)(3)== True, "ERREUR UNION"
    print("-"*50)

    print("car_S6")
    print("ajout(2, car_S3)(2) : ", ajout(2, car_S3)(2))
    assert ajout(2, car_S3)(2) == True, "ERREUR AJOUT"
    print("-"*50)

    print("Ensemble")
    print("ensemble([1,2,3,4,5])(6) : ",ensemble([1,2,3,4,5])(6))
    print("ensemble([1,2,3,4,5])(5) : ",ensemble([1,2,3,4,5])(5))
    assert ensemble([1,2,3,4,5])(5) == True, "ERREUR ENSEMBLE"
    print("-"*50)

    print("Fact")
    print(5*4*3*2*1)
    print("fact_main(5) : ",fact_main(5))
    print("fact_lambda(5) : ",fact_lambda(5))
    assert fact_main(5) == 5*4*3*2*1, "ERREUR FACT"
    print("-"*50)

    print("SOMME DES CARRE")
    print("somme_des_carres([1,2,3,4]) : ",somme_des_carres([1,2,3,4]))
    assert somme_des_carres([1,2,3,4]) == (1**2+2**2+3**2+4**2), "ERREUR SDC"
    print("-"*50)

    print("MAXIMUM")
    print("maximum([1,2,13,4]) : ",maximum([1,2,13,4]))
    assert maximum([1,2,13,4]) == 13, "ERREUR MAX"
    print("-"*50)

    print("FST")
    print("fst([(1,188),(2,154),(3, 12462)]) : ",fst([(1,188),(2,154),(3, 12462)]))
    assert fst([(1,188),(2,154),(3, 12462)]) == [1,2,3], "ERREUR FST"
    print("-"*50)

    print("PERMUTE")
    print("permute([0,1,0,1,0,1]) : ", permute([0,1,0,1,0,1]))
    assert permute([0,1,0,1,0,1]) == [1,0,1,0,1,0], "ERREUR PERMUTE"
    print("-"*50)

    print("COMPTE 0")
    print("compte0([0,1,0,1,0,1]) : ", compte0([0,1,0,1,0,1]))
    assert compte0([0,1,0,1,0,1]) == 3, "ERREUR COMPTE0"
    print("-"*50)

    print("PGS")
    print("pgs(3,[1,1,2,3,3,3,3,4,4,3,3]) : ",pgs(3,[1,1,2,3,3,3,3,4,4,3,3]))
    assert pgs(3,[1,1,2,3,3,3,3,4,4,3,3]) == 4, "ERREUR PGS"
    print("-"*50)

    print("=====> TOUS LES ASSERTS VALIDES <=====")

    

    





















