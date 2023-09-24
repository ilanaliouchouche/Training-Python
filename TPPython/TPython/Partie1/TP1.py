import math
import random
from functools import reduce
from itertools import cycle


def intersection():
    a = int(input("rentrer a : "))
    b = int(input("rentrer b : "))
    c = int(input("rentrer c : "))
    d = int(input("rentrer d : "))
    try:
        return round((d - b) / (a - c),2)
    except ZeroDivisionError:
        print("Les droites sont parallèles")

def power_2():
    n = int(input("rentrer n : "))
    def bis(n=n, acc=1):
        if n == 0:
            return acc
        else:
            return bis(n-1, 2*acc)
    return bis()


def somme():
    n = int(input("rentrer n : "))
    res2 = 0
    for i in range(1, n + 1):
        res2 += i
        if i == n:
            print(f"{i} =", end=' ')
        else:
            print(f"{i} +", end=' ')
    
    assert (res2 == (n * (n + 1) / 2)), "Erreur dans somme "   
    print(f"{res2}")
    return res2



def revenus():
    s = int(input('somme initiale : '))
    t = int(input('taux d\'intérêt : ')) / 100
    n = int(input('ancienneté : '))

    def calcul(s: int, t: float, n: int):
        if n == 0:
            print(f'total : {s}')
            return s
        else:
            y: int = calcul(s, t, n - 1)
            print(f'gain année {n} : {y * t}')
            total = y + y * t
            print(f'total année {n} : {total}')
            return total

    calcul(s, t, n)


from turtle import *  #pas bien mais on risque pas d'importer autre chose qui risque de masquer


def escalier(pos):
    pos.left(90)
    pos.forward(50)
    pos.right(90)
    pos.forward(50)


def n_escalier():
    n = int(input("rentrer n : "))
    init = Turtle()
    screen = init.screen
    screen.bgcolor("black")
    init.pencolor("yellow")
    init.pensize(25)
    init.hideturtle()
    init.penup()
    init.goto(-300, -300)
    init.pendown()
    for i in range(n):
        escalier(init)
    init.forward(200)
    done()

def grille(c=50):
    n = int(input("lignes : "))
    m = int(input("colonnes : "))
    turtle = Turtle()
    turtle.hideturtle()
    turtle.pensize(25)
    screen = turtle.screen
    screen.bgcolor("black")
    turtle.pencolor("yellow")
    #colonnes
    for i in range(m + 1):
        turtle.penup()
        turtle.goto(i * c, 0)
        turtle.pendown()
        turtle.goto(i * c, n * c)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.pencolor("pink")
    #lignes
    for i in range(n + 1):
        turtle.penup()
        turtle.goto(0, i * c)
        turtle.pendown()
        turtle.goto(m * c, i * c)
    done()

#mode classique
def fibo(n):
    x = 0
    if n == 1:
        x = 1
    elif n != 0:
        x = 1
        x2 = 0
        for i in range(2, n + 1):
            x, x2 = x + x2, x

    return x

#mode gen mieux pour la spirale
def fibo_gen():
    x = 1
    x2 = 0
    yield x2
    yield x
    while True:
        x, x2 = x + x2, x
        yield x


def spirale_fibo():
    n = int(input("rentrer n : "))
    spi = Turtle()
    spi.screen.bgcolor("black")
    colori = cycle(["pink", "green","yellow","brown", "blue", "orange"]) #un peu comme un gen inf 
    spi.pensize(11)
    spi.speed(200)
    spi.hideturtle()
    gen = fibo_gen()
    for i in range(n):
        spi.pencolor(next(colori))
        spi.circle(2*next(gen), 90)
    done()



def divis():
    n = int(input("rentrer n : "))

    def bis(n=n, cst=n):
        if n == 0:
            print('')
        else:
            if cst % n == 0:
                print(n, end=', ')
            bis(n - 1, cst)

    bis()


def billard(longueur=50, largeur=100):
    x = int(input('x : '))
    y = int(input('y : '))
    dx = int(input('dx : '))
    dy = int(input('dy : '))

    x_nouveau = x + dx
    y_nouveau = y + dy

    if x_nouveau < 0 or x_nouveau > longueur:
        dx *= -1
        x_nouveau = x + dx

    if y_nouveau < 0 or y_nouveau > largeur:
        dy *= -1
        y_nouveau = y + dy

    return x_nouveau, y_nouveau


def seconddegré(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        print(f'delta {delta} donc une solution')
        return [(-b) / (2 * a)]
    elif delta < 0:
        raise ValueError("Pas de solution")
    else:
        print(f'delta : {delta} donc deux solutions')
        return [format(-b - math.sqrt(delta) / (2 * a), '.2f'), format(-b + math.sqrt(delta) / (2 * a), '.2f')]



def occurences(v, t):
    return reduce(lambda acc, x: acc + 1 if x == v else acc, t, 0)



def tirage():
    res = {i: 0 for i in range(1, 11)}
    for i in range(1000):
        n = random.randint(1, 10)
        res[n] += 1
    return res


def echange(t, i, j):
    t[i], t[j] = t[j], t[i]



def melange(tab):
    taille = len(tab)
    for i in range(taille):
        j = random.randint(0, i)
        echange(tab, i, j)



def hamming(tab1, tab2):
    res = 0
    if len(tab1) != len(tab2):
        raise Exception('tableaux de différentes tailles')
    else:
        for i in range(len(tab1)):
            if tab1[i] != tab2[i]:
                res += 1
        return res



def chiffre(n):
    if n < 0:
        raise ValueError('NEGATIF')
    str_n = str(n)
    return len(str_n)



def sous_mot(a, b, tab):
    a_find = False
    for i in range(len(tab)):
        if tab[i] == a:      # on considere pos de b strict > pos de a
            a_find = True
        else:  # a == b déjà fait
            if tab[i] == b & a_find: 
                return True
    return False



def pgs(e, tab):   #peut être fait avec reduce
    maxi = 0
    cpt = 0
    for i in range(len(tab)):
        if tab[i] == e:
            cpt += 1
        else:
            cpt = 0
        if cpt > maxi:
            maxi = cpt
    return maxi

#version nulle en "mode python" peu opti.(REGARDER CELLE D'EN BAS)
def pgpc(tab1, tab2):
    cpt = 0
    #un peu couteux de parcourir les deux tableaux
    size = len(tab1) if len(tab1) < len(tab2) else len(tab2)
    #puis d'en reparcourir un
    for i in range(size):
        if tab1[i] == tab2[i]:
            cpt += 1
        else:
            return cpt
    return cpt

#Version un peu mieux car on calcule pas les len avant, donc complexite = taille plus petit tableau
def pgpc2(tab1, tab2):
    i = 0
    while True:
        try:
            if (tab1[i] != tab2[i]):
                break
        except IndexError: #l'exception sert a savoir si on est out of range.
            break
        i += 1
    return i
        

def multiplication():
    size = range(1, 11)
    for i in size:
        print(f'\nTable de {i} : \n')
        for j in size:
            print(f'{i} * {j} = {i * j}')



def tab2D(tab):
    minis = map(min, tab)
    return max(minis)

#hanoi si on sait le faire pour n - 1 on sait le faire pour n, il
# faut se retrouver a l'etape ou les n - 1 sont dans l'intermediaire
# puis on bouge le dernier disque vers le piquet de fin et finalement
#on deplace le pack d'n-1 vers la fin
 
def hanoi(n, debut=1, inter=2, arrive=3):
    if n==1:
        print(f"Move {debut} on {arrive}")
    else:
        #n-1 vers l'intermediaire en s'aidant de l'arrivee
        hanoi(n-1,debut, arrive, inter)
        #le n eme n le bouge du debut a la fin
        print(f"Move {debut} on {arrive}")
        #puis n-1 vers la fin
        hanoi(n-1, inter, debut, arrive)




def koch(n, l):
    if n==0:
        forward(l)
    else:
        koch(n-1,l/3)
        left(60)
        koch(n-1,l/6)
        right(120)
        koch(n-1, l/6)
        left(60)
        koch(n-1,l/3)


if __name__ == "__main__":
    #print(intersection())
    
    #print(power_2())

    #somme()

    #revenus()

    #n_escalier()

    #grille()

    #spirale_fibo()

    #divis()

    #print(billard())

    #print(seconddegré(1,4,1))

    #print(occurences(5, [5,1,1,1,1,1,5,1,5]))

    #print(tirage())

    #t = [1,2,3,4,5]
    #print(t)
    #melange(t)
    #print(t)

    #print(hamming([1, 2, 3, 4, 5], [1,3,3,4,4]))

    #print(chiffre(100))

    #print(sous_mot(0,1,[1,0,0,0,0]))
    #print(sous_mot(1,0,[0,0,0,1,1,1]))
    #print(sous_mot(1,0,[0,0,0,1,0,1]))

    #print(pgs(1,[0,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0]))

    #print(pgpc([1,2,3,4],[1,2,3,5]))
    #print(pgpc2([1,2,3],[1,2,3,5,6,7]))

    #print(multiplication())

    #print(tab2D([[1,2,3,4],
           #[0,0,0,0],
           #[5,5,5,4]]))
    
    #hanoi(3)


    #dé commenter le reste pur koch

    #hideturtle()
    #speed(100)
    #bgcolor("black")
    #pencolor("yellow")
    #koch(3,500)
    #exitonclick()

    print("",end='')






