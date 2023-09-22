from abc import ABC, abstractmethod

class Rope(ABC):
    def __init__(self):
        self.length = 0
    @abstractmethod
    def __getitem__(self,i):
        pass
    @abstractmethod
    def __add__(self,r):
        pass
    @abstractmethod
    def __str__(self):
        pass
    #celle ci est pour la dernière question.
    @abstractmethod
    def path(self):
        pass

#QUESTION 1

#On peut creer une classe de cette manière.

class Str(Rope):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.length = len(self.value)

    def __str__(self):
        pass
    def __add__(self,r):
        pass
    def __getitem__(self,i):
        pass
    #same
    def path(self):
        pass

class App(Rope):
    def __init__(self, g:Rope, d:Rope):
        super().__init__()
        self.g = g
        self.d = d
        self.length = g.length + d.length
    def __str__(self):
        pass
    def __add__(self,r):
        pass
    def __getitem__(self,i):
        pass
    def path(self):
        pass

'''


On peut aussi créer de cette maniere en python car une classe 
est un objet, une instance d'une métaclasse. 
La métaclasse mère de toute est type.


'''

Str2 = type("Str2",(Rope,), {})  #Nom qu'on veut, Classe(s) mère(s), attributs/methodes.
App2 = type("App2",(Rope,), {})

print(Str)
print(App)
print("Les classes faites avec 'type' vont être abstraites car il faudrait réimplémenter les méthodes abstraites de Rope à l'extérieur puis les associer à la classe "
      "avec cette syntaxe :\n 'Classe.methode = fonction'")
print(Str2) 
print(App2)

r = App(Str('La structure de'),
App(App(Str('corde per'),Str('met de manipuler')),
App(Str(' de grandes '),Str('chaînes'))))

#QUESTION 2 

def str_str(self):
    return self.value

def app_str(self):
    return str(self.g) + str(self.d)

Str.__str__ = str_str

App.__str__ = app_str

print("-"*50)
print("Questiion 2 : ", r)

#QUESTION 3

def str_getitem(self,i):
    return self.value[i]

def app_getitem(self,i):
    if i < self.g.length:
        return self.g[i]
    return self.d[i - self.g.length]

Str.__getitem__ = str_getitem

App.__getitem__ = app_getitem

print("-"*50)
print("Question 3 :")
print(r[6])
print(r[16])

#QUESTION 4

def str_getitem2(self,i):
    if isinstance(i, slice):
        return self.value[i.start:i.stop] 
    return str_getitem(self, i)

def app_getitem2(self, i):
    if isinstance(i, slice):
        if i.stop <= self.g.length:
            return self.g[i.start:i.stop]
        if i.start >= self.g.length:
            return self.d[i.start - self.g.length:i.stop - self.g.length]
        return self.g[i.start:self.g.length] + self.d[0:i.stop - self.g.length]
    return app_getitem(self, i)

Str.__getitem__ = str_getitem2

App.__getitem__ = app_getitem2

print("-"*50)
print("Question 4 : ", r[21:54])

#QUESTION 5

def app_add(self, rope):
    if self.length + rope.length < 10:
        return Str(str(self) + str(rope))
    if self.d.length + rope.length < 10:
        #on test si on peut ajouter au niveau du fils droit de self.
        return App(self.g, Str(str(self.d) + str(rope)))
    if isinstance(rope, App):
        #ici on pourrait faire quelque chose de récursif qui
        #qui creerait un app(self.g, self.d + rope) cependant
        #cela creéra des filiformes et dédomagera la complexité
        # de nos ropes. Ainsi, on va juste tester si on peut rejoindre
        #d'une quelconque manière avec les enfants.
        if self.length + rope.g.length < 10:
            return App(Str(str(self) + str(rope.g)), rope.d)
    # si instance de rope est Str : on à déjà fait ce qu'on pouvait
    return App(self, rope) 


def str_add(self, rope):
    #si les deux arbres ont une taille < 10
    if self.length + rope.length < 10 :
        return Str(str(self) + str(rope))
    #donc rope + self > 10 on voudrait chercher à faire une recursion
    # à gauche pour voir si on peut joindre deux chaines,
    #cependant si on laisse pour tous les cas, nos ROPE pourraient
    #devenir des filiformes, on va donc laisser une chance seulement au 
    # fils de gauche de pouvoir se concatener à self. 
    if isinstance(rope, App) :
        if (rope.g.length + self.length) < 10:
            return App(Str(str(self)+str(rope.g)),rope.d)
    #on a finit de descendre sur rope ou on a deux str avec leur
    #taille cumulée supérieur à 10.
    return App(self, rope)

def path_str(self):
    chain = f"Str({self.value})"
    return chain
def path_add(self):
    chain = f"App({self.g.path()}, {self.d.path()})"
    return chain

Str.__add__ = str_add
App.__add__ = app_add
Str.path = path_str
App.path = path_add



r2 = (Str('debut de la ') + Str('chai')) + Str('ne')
print(r2.path())


        

        

        
























