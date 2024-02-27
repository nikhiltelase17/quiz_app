from tkinter import *
from quiz_brain import QuizBrain
import pygame

BACKGOUND = pygame.mixer.Sound("sounds/backgound.mp3")
GAME_OVER = pygame.mixer.Sound("sounds/game_over.mp3")
pygame.mixer.Sound.play(BACKGOUND)

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg=THEME_COLOR)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     width=280,
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=right_img, bg=THEME_COLOR, command=self.true_pressed, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=wrong_img, bg=THEME_COLOR, command=self.false_pressed, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            # completed all questions than do this
            pygame.mixer.Sound.stop(BACKGOUND)
            pygame.mixer.Sound.play(GAME_OVER)
            self.canvas.config(bg="yellow")
            self.canvas.itemconfig(self.question_text,
                                   text=f"You completed quiz\nYour final score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        # is_right True or False ho sakta hai
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        # is_right True or False ho sakta hai
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.quiz.score += 1
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
