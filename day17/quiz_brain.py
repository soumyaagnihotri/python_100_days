class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text}(True/False):")
        self.question_number += 1
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, u_a, c_a):
        if u_a.lower() == c_a.lower():
            self.score +=1
            print("Your answer is correct")

        else:
            print("Your answer is wrong")
        print(f"{c_a} is correct answer")
        print(f"Your score is {self.score}/{self.question_number}\n")
