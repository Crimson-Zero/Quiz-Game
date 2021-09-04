
class Quiz_Brain:
    
    def __init__(self,question_bank):
        
        self.question_number=0
        self.question_list=question_bank
        self.score=0
    
    def still_has_questions(self):
        
        return(self.question_number<len(self.question_list))
    
    def get_next_question(self):
        
        self.current_question=self.question_list[self.question_number].question
        self.correct_answer=self.question_list[self.question_number].answer
        self.question_number+=1
        print(f"Q.{self.question_number}: {self.current_question} (True/False)")
       
        return(self.current_question)
    
    def check_answer(self):
        
        self.answer=input("Enter True or False:")
       
        if(self.answer==self.correct_answer):
            print("You are Correct")
            self.score+=1
        else:
            print("The answer given was incorrect")
    
    def get_score(self):
        
        print(f"Your Total score is : {self.score}")
        return(self.score)
        
        

    

        
        