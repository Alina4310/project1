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




a = [23, 344, 243, 2, 8667, 43, 45, 1, 17, 55, 62]
for i in range(len(a)):
    if a[i] % 2 ==0:
        print(a[i])
        a[i] = 0
    if a[i] % 2 == 1:
        a[i] = 1
print(a)

count = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        count += 1

print(count)
