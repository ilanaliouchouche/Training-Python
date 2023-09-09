from collections import Counter
from functools import reduce
from statistics import mean
import sys


def stats2(file):
    with open(file, "r") as f:

        #lignes
        lines = f.readlines()
        print(f"Nombre de lignes : {len(lines)}")

        #mots
        words = [word.lower() for line in lines for word in line.split()]
        print(f"Nombre de mots : {len(words)}")

        #caracteres
        char_count = sum(len(line) for line in lines)
        print(f"Nombre de caractères : {char_count}")

        #mot le + frequent
        count_words = Counter(words)
        most_common_word, _ = count_words.most_common(1)[0]
        print(f"Mot le plus fréquent : {most_common_word}")

        #le + long
        longest_word = reduce(lambda acc, w: w if len(w) > len(acc) else acc, words, '')
        print(f"Mot le plus long est : {longest_word}")

        #moyenne de mots par lignes
        words_per_line = [len(line.split()) for line in lines]
        mean_words = mean(words_per_line)
        print(f"Moyenne du nombre de mots par ligne: {mean_words:.2f}")

        #lettre la + frequente
        all_chars = [char for line in lines for char in line.lower() if char.isalpha()]
        most_common_char, _ = Counter(all_chars).most_common(1)[0]
        print(f"Lettre la plus fréquente est : {most_common_char}")


if __name__ == "__main__":
    argv = sys.argv[1]

    stats2(argv)