import questions
import random 
temp = []
score = 0
b = True
while b is True: 
    question = random.choice(list(questions.bank.keys()))
    ans = questions.bank[question]
    print("\n\nCurrent score: ", score, "\n-----------------\n\n")
    print(question)
    answer = input( "\n\nYour answer(type 'exit()' to exit': ")
    if answer is not ans:
       b = False 
    score += 1
