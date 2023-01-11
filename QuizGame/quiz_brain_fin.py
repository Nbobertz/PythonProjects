class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list1 = question_list
        self.points = 0

    def out_of_questions(self):
        return self.question_number < int(len(self.question_list1))





    def next_question(self):
        current_question = self.question_list1[self.question_number]
        choice = input(f"Question {self.question_number + 1}: {current_question.text} [True] or [False]").capitalize()
        self.question_number += 1
        correct = (current_question.answer)
        if choice == correct:
            self.points += 1
            print("You are correct")
        else:
            print(f"You are wrong! The correct answer is {current_question.answer}")
        print(f"You have {self.points} points\n")