import sys

def cut(file, sep, inter):
    #on setup les colonnes qu'on veut
    indexs = []
    for s in inter.split(','):
        bornes = s.split('-')
        interv = list(range(int(bornes[0]) - 1, int(bornes[1])))
        indexs.extend(interv)
    #on met sous forme d'ensemble puis de liste pour avoir les indexs uniques
    indexs = list(set(sorted(indexs)))
    with open(file, 'r') as f:
        for line in f:
            #on recupere le tableau des different elements en fonction du sep et enlevant les /n et /s
            tokens = line.strip().split(sep)

            #on recupere les tokens qu'on veut et possibles
            res = [tokens[i] for i in indexs if i < len(tokens)]
            #on affiche dans la même forme
            print(sep.join(res))


if __name__ == '__main__':
    argv = sys.argv
    #on recupere l'element apres -d
    sep = argv[argv.index("-d") + 1]
    #same pour -f
    interv = argv[argv.index("-f") + 1]
    #on appelle
    cut(argv[-1],sep, interv)