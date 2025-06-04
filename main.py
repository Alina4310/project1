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

