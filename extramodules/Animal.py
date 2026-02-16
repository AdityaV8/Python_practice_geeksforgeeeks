import json

with open('questions.json', 'r') as f:
    questions = f.read()
    
data = json.loads(questions)
for question in data:
    print(question["Question_text"])
    for index,alternative in enumerate(question["alternatives"]):
        print(index+1," ",alternative)
    user_choice = int(input("Enter your choice : "))
    question["user_choice"] = user_choice

score = 0
for index,question in enumerate(data):
    if question["user_choice"] == question["Correct_ans"]:
        score += 1
        result = "So Correct ! "
    else:
        result = "oops Wrong ! "
    message = f"{index+1}. Your answer: {question['user_choice']},"+\
        f"  Correct answer: {question['Correct_ans']},"+\
        f" {result}"
    print(message)
    
print(f"Your score is : {score}")
