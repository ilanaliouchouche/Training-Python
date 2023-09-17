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

###On peut aussi créer de cette maniere en python car une classe est un objet, une instance d'une métaclasse. La métaclasse mère de toute est type.

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

def str_add(self, rope):
    if isinstance(rope, Str):
        if self.length + rope.length < 10:
            return Str(self.value + rope.value)
    elif isinstance(rope, App):
        if rope.length + self.length < 10:
            return Str(self.value + str(rope))
        elif isinstance(rope.g, Str) and (rope.g.length + self.length < 10):
            return App(Str(self.value + rope.g.value), rope.d)
        elif isinstance(rope.g, App) and (rope.g.length + self.length < 10):
            return App(self + rope.g, rope.d)
    return App(self, rope)

def str_app(self, rope):
    if isinstance(rope, Str):
        if self.length + rope.length < 10:
            return Str(str(self) + rope.value)
        elif isinstance(self.d , Str) and (self.d.length + rope.length < 10):
            return App(self.g, self.d.value + rope.value)
        elif isinstance(self.d, App) and (self.d.length + rope.length < 10):
            return App(self.g, Str(str(self.d) + rope.value))
    if isinstance(rope, App):
        if self.length + rope.length < 10:
            return Str(str(self) + str(rope))
        #c'est ici qu'on va eviter de creer des filiformes en regardant a droite et a gauche. si pas de solution on fait pas de filiforme on rajoute un noeud
        elif isinstance(self.d, Str) and isinstance(rope.g, Str) and (self.d.length + rope.g.length < 10):
            nouveau = Str(self.d.value + rope.g.value)
            if (nouveau.length + rope.d.length < 10):
                return App(self.g, Str(nouveau.value + str(rope.d)))
            elif (nouveau.length + self.g.length < 10):
                return App(Str(str(self.g) + nouveau.value), rope.d)
        elif isinstance(self.d, App) and isinstance(rope.g, Str) and (self.d.length + rope.g.length < 10):
            if self.d.length + rope.g.length < 10:
                nouveau = Str(str(self.d.length) + rope.g.value)
                if (nouveau.length + rope.d.length < 10):
                    return App(self.g, Str(nouveau.value + str(rope.d)))
                elif (nouveau.length + self.g.length < 10):
                    return App(Str(str(self.g) + nouveau.value), rope.d)
        #je me suis perdu...

            


         



Str.__add__ = str_add

r2 = (Str('debut de la ') + Str('chai')) + Str('ne')

print(r2)
        

        

        
























