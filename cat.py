import sys
def cat(*args):
    for f in args:
        with open(f, "r") as f1:
            for line in f1:
                print(line)


if __name__ == '__main__':
    argv = sys.argv[1:]
    cat(*argv)
