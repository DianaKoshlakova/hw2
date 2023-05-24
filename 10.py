# Задача 10: На столе лежат n монеток. Некоторые из них 
# лежат вверх решкой, а некоторые – гербом. Определите 
# минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же 
# стороной. Выведите минимальное количество монет, которые
# нужно перевернуть.

n = int(input("Введите число n: "))
countG = 0 # гербы
countR = 0 # решки
for i in range(n):
    x = int(input("Если решка, введите 1, если герб - 0: "))
    if x == 1 :
            countR +=1
    elif x == 0 :
        countG +=1
    else :
         print("Запрос введён некорректно!")
if countG >= countR :
    print(f"Нужно перевернуть {countR}")
else :
    print(f"Нужно перевернуть {countG}")