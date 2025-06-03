score = 0
total_questions = 5
print("How old are you?")
N = int(input())
if N <= 18:
    print("Hi!")
else:
    print("Good afternoon!")
answer = input("Are you ready? (yes/no) ")
if answer == "yes":
    print("Let's go!")
else:
    print("We will wait")
answer = input("What is the capital of Russia?")
if answer =="Moscow":
    score += 1
    print("Perfect!")
else:
    print("incorrect")
answer = input("What is the capital of France?")
if answer =="Paris":
    score += 1
    print("Correct")
else:
    print("Incorrect")
answer = input("What is the capital of Spain?")
if answer =="Madrid":
    score += 1
    print("Very good")
else:
    print("Incorrect")
answer = input("What is the capital of Germany?")
if answer =="Berlin":
    score += 1
    print("Perfect!")
else:
    print("Incorrect")
answer = input("What is the capital of Italy?")
if answer =="Rome":
    score += 1
    print ("Correct!")
else:
    print("Incorrect")
mark = (score/total_questions)*100
print(mark)