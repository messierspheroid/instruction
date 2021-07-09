from tkinter import *
from quiz_brain import QuizBrain

# putting quizbrain objects onto the screen to be displayed


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # row 0
        self.score_l = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_l.grid(column=1, row=0, columnspan=2)

        # row 1
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Some Question Text",
            font=THEME_COLOR, fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # row 2
        true_png = PhotoImage(file="images/true.png")
        self.true_b = Button(
            image=true_png, highlightthickness=0, command=self.true_pressed
        )
        self.true_b.grid(column=0, row=2)

        false_png = PhotoImage(file="images/false.png")
        self.false_b = Button(
            image=false_png, highlightthickness=0, command=self.false_pressed
        )
        self.false_b.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_l.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # end of quiz text
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # right or wrong background changes
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
