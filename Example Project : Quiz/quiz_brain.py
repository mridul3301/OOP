class QuizBrain:

    def __init__(self, question_list):
        self.question = question_list
        self.score = 0
        for i in self.question:
            self.next_question(i, self.question.index(i))

    def next_question(self, que, qn):
        current_question = que.text
        current_answer = que.answer
        player_answer = input(f"Q.N. {qn} : {current_question} (True/False) \n")
        self.check_answer(current_answer, player_answer, qn)

    def check_answer(self, current_answer, player_answer, qn):
        if current_answer == player_answer.capitalize():
            print("Correct Answer!!")
            self.score += 1
        elif player_answer.capitalize() != "True" and player_answer.capitalize() != "False":
            print("WRONG!!!!!! Answer should be Either true or False. Other answer are automatically considered wrong")
        else:
            print("Wrong Answer!")

        print(f"Your final score is : {self.score}/{qn+1}")