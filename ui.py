import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.configure(bg=THEME_COLOR)

        self.canvas = tk.Canvas(self.window, width=250, height=300, bg='white')
        self.question_text = self.canvas.create_text(125, 150,
                                                     fill=THEME_COLOR,
                                                     text='PLaceholder Question',
                                                     font=('Arial', 18, 'italic'),
                                                     width=250
                                                     )

        self.label = tk.Label(self.window, text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white')
        self.img_true_btn = tk.PhotoImage(file='./images/true.png')
        self.img_false_btn = tk.PhotoImage(file='./images/false.png')
        self.true_btn = tk.Button(self.window, image=self.img_true_btn, highlightthickness=0, bd=0,
                                  command=lambda: self.check_question('True'))
        self.false_btn = tk.Button(self.window, image=self.img_false_btn, highlightthickness=0, bd=0,
                                   command=lambda: self.check_question('False'))

        self.label.grid(row=1, column=2, pady=20)
        self.canvas.grid(row=2, column=1, columnspan=2, padx=20, pady=20)
        self.true_btn.grid(row=3, column=1, pady=20)
        self.false_btn.grid(row=3, column=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def check_question(self, user_answer):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer(user_answer):
                print('correct')
                self.update_score()
                self.give_feedback(True)
            else:
                print('wrong')
                self.give_feedback(False)
        else:
            self.canvas.itemconfig(self.question_text, text='End Of Quiz Reached')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')


    def update_score(self):
        self.label.config(text=f'Score: {self.quiz.score}')

    def give_feedback(self, true_false: bool):
        if true_false:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, lambda: self.reset_color_canvas())

    def reset_color_canvas(self):
        self.canvas.config(bg='white')
        self.window.after(500,self.get_next_question())
