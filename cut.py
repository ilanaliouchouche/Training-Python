import sys

def cut(file, sep, inter):
    indexs = []
    for s in inter.split(','):
        s_ar = s.split('-')
        interv = list(range(int(s_ar[0]) - 1, int(s_ar[1])))
        indexs.extend(interv)
    indexs = list(set(sorted(indexs)))
    with open(file, 'r') as f:
        for line in f:
            tokens = line.strip().split(sep)

            res = [tokens[i] for i in indexs if i < len(tokens)]

            print(sep.join(res))


if __name__ == '__main__':
    argv = sys.argv
    sep = argv[argv.index("-d") + 1]
    interv = argv[argv.index("-f") + 1]
    cut(argv[-1],sep, interv)
