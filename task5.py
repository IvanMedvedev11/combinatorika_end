from itertools import combinations
def combination(word, cnt):
    combos = combinations(word, cnt)
    counts = 0
    for combo in combos:
        if combo.count('a') == 3 and combo.count('b') == 2:
            print(*combo)
            counts += 1
    print(counts)
cnt = int(input("Введите кол-во символов: "))
word = input("Введите слово: ")
combination(word, cnt)
