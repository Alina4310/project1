question = "Какой сегодня месяц?"
right_answer = "июнь"

print(question)
user_answer = input()
while user_answer != right_answer:
    print("Wrong! Try again.")
    user_answer = input()

print("Well done")
