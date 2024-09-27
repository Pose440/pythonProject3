import random
from random import choice


def area():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    cipher = random.choice(num)
    return cipher
def area2(i):
    dict = {}
    dict.update({3 : 12, 4 : 13, 5 : 1423, 6 : 121524, 7 : 162534, 8 : 13172635, 9 : 1218273645, 10 : 141923283745})
    dict.update({11 : 11029384756, 12 : 12131511124210394857, 13 : 112211310495867, 14 : 1611325212343114105968})
    dict.update({15 : 1214114232133124115106978, 16: 1317115262143531341251161079, 17 : 11621531441351261171089})
    dict.update({18 : 12151811724272163631545414513612711810, 19 : 118217316415514613712811910})
    dict.update({20 : 13141911923282183731746416515614713812911})
    passcode = dict.get(i)
    return passcode
i = area()
print(i)
pair1 = list(range(1, i))
pair2 = list(range(1, i))
pairs = []
result = ""
for k in pair1:
    for l in pair2:
        p1 = k
        p2 = l
        if p1 >= p2:
            continue
        else:
            kratno = i % (p1 + p2)
            if kratno == 0:
                pairs.append([p1, p2])
                result = result + str(p1) + str(p2)
print(*pairs)
print(result)
if int(result) == area2(i):
   print("Проходите")
