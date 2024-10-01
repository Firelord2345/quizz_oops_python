from data import question_data
from question_model import question
from quiz_brain import Quizzbrain
question_bank=[]
for q in question_data:
    q_text=q["text"]
    q_answer=q["answer"]
    question_new=question(q_text,q_answer)
    question_bank.append(question_new)
# print(question_bank[0].answer)  
qu=Quizzbrain(question_bank)
while qu.questionno<len(question_bank):
   qu.nextquestion()
   
print("Hurray Completed")
print(f"score {qu.score}/{len(question_bank)}")   