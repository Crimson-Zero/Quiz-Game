
from quiz_question_model import Quiz_Store
from quiz_game_data import question_data
from quiz_brain import Quiz_Brain

test_data=[]

for data in range(len(question_data)):
    quiz_object=Quiz_Store(question_data[data]['text'],question_data[data]['answer'])
    test_data.append(quiz_object)


testing=Quiz_Brain(test_data)

while testing.still_has_questions()==True:
    testing.get_next_question()
    testing.check_answer()

testing.get_score()
