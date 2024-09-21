from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz

        # Setup window
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        # Score
        self.score_label = Label(text=f"Score: 0", background=THEME_COLOR, font=("Arial", 12), fg="white")
        self.score_label.grid(row=0, column=1)

        # Question Canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   text=f"{self.quiz_brain.next_question}",
                                                   font=("Arial", 20, "italic"),
                                                   width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Right button (Correct)
        right_button_image = PhotoImage(file="images/true.png")
        self.right_button = Button(width=100, height=97,
                                   image=right_button_image,
                                   command=self.check_true)
        self.right_button.grid(row=2, column=1)

        # Left button (Wrong)
        left_button_image = PhotoImage(file="images/false.png")
        self.left_button = Button(width=100, height=97,
                                  image=left_button_image,
                                  command=self.check_false)
        self.left_button.grid(row=2, column=0, pady=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            # Change score and display next question
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question)
        else:
            # If quiz is finished display text and disable buttons
            self.canvas.itemconfig(self.canvas_text, text="You've completed the quiz.")
            self.right_button.config(state="disabled")
            self.left_button.config(state="disabled")

    # Functions to check for answers
    def check_false(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def check_true(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    # Function to flash green light if the user was right
    # and the red light if the user was wrong
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
