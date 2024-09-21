from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)
quiz_interface.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
