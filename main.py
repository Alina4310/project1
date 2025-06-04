from random import *

N = randint(1, 10)
Lives = 3

while Lives > 0:
    print("Осталось жизней:", Lives)
    print("Какое число загадано?")
    user_answer = int(input())
    if user_answer == N:
        print("Победа!")
        break
    elif N > user_answer and Lives > 1:
        print("Загаданное число больше")
    elif N < user_answer and Lives > 1:
        print("Загаданное число меньше")
    Lives -= 1
    if user_answer < 1 or user_answer > 10:
        print("Число должно быть от 1 до 10 включительно")
        Lives += 1
if Lives == 0:
    print("Вы проиграли")
print ("Было загадано число", N)
print("Конец игры.")