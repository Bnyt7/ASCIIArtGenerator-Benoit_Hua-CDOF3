import requests
import json
import random


amount = 10
difficulty = ["easy","medium","hard"]

response = requests.get("https://opentdb.com/api.php?amount="+str(amount)+"&difficulty="+difficulty[0]+"&type=multiple")

data = response.json()
"""def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())"""

results = data["results"]

# Extract arrays
categories = [item["category"] for item in results]
questions = [item["question"] for item in results]
correct_answers = [item["correct_answer"] for item in results]
incorrect_answers = [item["incorrect_answers"] for item in results]
difficulties = [item["difficulty"] for item in results]

# Display arrays
#print("Categories:", categories)

#print("Questions:", questions)

#print("Correct Answers:", correct_answers)

#print("Incorrect Answers:", incorrect_answers)

#print("Difficulties:", difficulties)

def question(number, categories,questions,correct_answers,incorrect_answers,difficulties):
    print("Question number "+str(number))
    print(categories[number])
    print(difficulties[number])
    print(questions[number])


def shuffleAnswers(number, correct_answers, incorrect_answers):
    answers = []
    answers.append(correct_answers[number])
    for i in incorrect_answers[number]:
        answers.append(i)
    random.shuffle(answers)
    return answers



question(1,categories,questions,correct_answers,incorrect_answers,difficulties)
answ = shuffleAnswers(1,correct_answers,incorrect_answers)
print(answ)