from question_model import Question

from data import question_data

from quiz_brain import QuizBrain

question_Bank = []

for i in question_data:
    question_Bank.append(Question(i["text"], i["answer"]))

while 1:
    ans = input("Do you want to play the game (Y/N)?").lower()
    if ans == "y":
        QuizBrain(question_Bank)
    else:
        exit()
