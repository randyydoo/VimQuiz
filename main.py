import questions
import random 
def main():
    temp = []
    score = 0
    while True:
        question = random.choice([questions.bank.keys()])
        while question in temp:
            question = random.choice([questions.bank.keys()])
        answer = questions.bank[question]
        print(f"Current score: {score} \n -------------------\n")
        ans = input(question, "Your answer(type 'exit' to exit': ")
        if ans is not answer:
            score = 0
            temp = []
            continue
        elif ans == "exit":
            break
        score += 1
        temp.append(question)
main()
