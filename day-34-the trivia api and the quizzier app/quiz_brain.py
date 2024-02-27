import html
import pygame

pygame.mixer.init()
CORRECT_ANS = pygame.mixer.Sound("sounds/correct.mp3")
WRONG_ANS = pygame.mixer.Sound("sounds/wrong.mp3")


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        que_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {que_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            pygame.mixer.Sound.play(CORRECT_ANS)
            return True
        else:
            pygame.mixer.Sound.play(WRONG_ANS)
            return False
