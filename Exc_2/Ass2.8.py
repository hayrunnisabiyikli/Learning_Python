correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

with open('student_answers.txt', 'r') as file:
    student_answers = file.readlines()

student_answers = [answer.strip().upper() for answer in student_answers]

num_correct = 0
num_incorrect = 0
incorrect_question_numbers = []
for i in range(len(correct_answers)):
    if student_answers[i] == correct_answers[i]:
        num_correct += 1
    else:
        num_incorrect += 1
        incorrect_question_numbers.append(i + 1)
print("Exam Result:")
if num_correct >= 15:
    print("Congratulations! You passed the exam.")
else:
    print("Sorry, you failed the exam.")
print("Total Correct Answers: ", num_correct)
print("Total Incorrect Answers: ", num_incorrect)
print("Incorrectly Answered Question Numbers: ", incorrect_question_numbers)
