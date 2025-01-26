from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# boş bir liste oluşturduk
question_bank = []

# question_data içindeki her bir soruyu alıp Question class'ından bir obje oluşturup question_bank listesine ekliyoruz
for question in question_data:
    question_text = question["soru"]
    question_answer = question["dogru_cevap"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

# QuizBrain class'ından bir obje oluşturduk ve question_bank listesini argüman olarak verdik
quiz = QuizBrain(question_bank)

# QuizBrain class'ındaki still_has_question methodunu kullanarak sorular bitene kadar soruları sormaya devam ediyoruz
while quiz.still_has_question():
    # QuizBrain class'ındaki next_question methodunu kullanarak bir sonraki soruyu soruyoruz
    quiz.next_question()

# QuizBrain class'ındaki score ve question_number attribute'lerini kullanarak kullanıcının kaç soruya doğru cevap verdiğini gösteriyoruz
print("You' ve complated the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
