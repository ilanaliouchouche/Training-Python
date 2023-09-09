import sys


def cat(*files):
    for i, file in enumerate(files):
        with open(file, "r") as f:
            print(f"Fichier{i} :")
            for line in f:
                print(line)
            print("\n\n")

if __name__ == '__main__':
    #on recup le fichiers en argument
    argv = sys.argv[1:]
    #on les passe dans cat
    cat(*argv)