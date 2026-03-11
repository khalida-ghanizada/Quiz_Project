class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.lower()




