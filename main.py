import questions
import random 
def main():
    temp = []
    score = 0
    while True:
        question, ans = random.choice(list(questions.bank.items()))
        while question in temp:
            question, ans = random.choice(list(questions.bank.items()))
        print("Current score: ", score, "\n\n-----------------")
        print(question)
        answer = input( "Your answer(type 'exit' to exit': ")
        if answer is not ans:
            score = 0
            temp = []
            continue
        elif answer == "exit":
            break
        score += 1
        temp.append(question)
main()
