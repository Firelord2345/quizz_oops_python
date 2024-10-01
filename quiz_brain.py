class Quizzbrain():
    def __init__(self,q_list):
        self.questionno=0
        self.score=0
        self.q_list=q_list
    def check(self,user_answer,actual_answer):
        if(user_answer.lower()==actual_answer.lower()):
            print("Correct Answer")
            self.score+=1
        else:
            print(f"Oops wrong answer,the correct answer is{actual_answer}")
    def nextquestion(self):
        current_question=self.q_list[self.questionno]
        self.questionno+=1
        user_answer=input(f"{self.questionno}> {current_question.text}True/False :")
        self.check(user_answer,current_question.answer)
    
    