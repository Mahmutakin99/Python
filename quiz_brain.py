class QuizBrain:
    # QuizBrain class'ı oluşturduk ve question_list adında bir attribute oluşturduk ayrıca 
    # question_number ve score adında iki default değere sahip attribute daha oluşturduk
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    # still_has_question methodu ile eğer question_number attribute'ü question_list'in uzunluğundan küçükse True döndürüyoruz
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    # next_question methodu ile question_number attribute'ünü 1 arttırıyoruz ve current_question adında bir değişken oluşturuyoruz 
    # ve bu değişkene question_list içindeki question_number indexindeki soruyu atıyoruz
    # daha sonra user_answer adında bir değişken oluşturuyoruz ve kullanıcıdan soruyu sormak için input alıyoruz
    # check_answer methodunu kullanarak kullanıcının verdiği cevabı kontrol ediyoruz
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer)

    # check_answer methodu ile kullanıcının verdiği cevabı ve doğru cevabı karşılaştırıyoruz
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("that's wrong")
        print(f"the correct answer was: {correct_answer}.")
        print(f"your current score is: {self.score}/{self.question_number}\n")
        