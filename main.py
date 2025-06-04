question = "Какой сегодня месяц?"
right_answer = "июнь"
k = 0
print(question)
user_answer = input()
while user_answer != right_answer:
    print("Wrong! Try again.")
    user_answer = input()
    k = k + 1
print("Well done, you used ",k," tries")

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
    elif N > user_answer:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    Lives -= 1
    if user_answer < 1 or user_answer > 10:
        print("Число должно быть от 1 до 10 включительно")
        Lives += 1

print ("Было загадано число", N)
print("Конец игры.")
