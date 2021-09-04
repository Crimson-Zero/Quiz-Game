
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
 



""""Notes Initiality the quiz question_model was initialized as the Quiz_Store class that 
had the attributes of the question and answer which were passed into it from the quiz_main.py
file 12 objects were created for the quiz_store using the loop this can be accomplished
with the range and len on the for question in question as the question data is a list
holding key value pairs."""