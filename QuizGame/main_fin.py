from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

##: Below I am going to make a list, build a range of how many questions, then go through and add each question to the
# list with a function
question_list = []
question_range = range(0,len(question_data))

for n in question_range:
    pull_out = question_data[n]
    list_question = Question(pull_out['text'], pull_out['answer'])
    question_list.append(list_question)
##: this keeps track of the points
quiz = QuizBrain(question_list)
while quiz.out_of_questions() != False:
    quiz.next_question()
print("You are out of questions!")
print(f"Your final score is {quiz.points}/{len(question_list)} points")





