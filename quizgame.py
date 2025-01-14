import requests
import json
import random
import html

amount = 10
difficulty = ["easy","medium","hard"]

response = requests.get("https://opentdb.com/api.php?amount="+str(amount)+"&difficulty="+difficulty[0]+"&type=multiple")

data = response.json()
results = data["results"]

# Extract arrays
categories = [item["category"] for item in results]
questions = [html.unescape(item["question"]) for item in results]
correct_answers = [html.unescape(item["correct_answer"]) for item in results]
incorrect_answers = [html.unescape(item["incorrect_answers"]) for item in results]
difficulties = [item["difficulty"].upper() for item in results]

# Display arrays
#print("Categories:", categories)

#print("Questions:", questions)

#print("Correct Answers:", correct_answers)

#print("Incorrect Answers:", incorrect_answers)

#print("Difficulties:", difficulties)

def question(number, categories,questions,correct_answers,incorrect_answers,difficulties):
    print("Question number "+str(number+1))
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

def showQuestions(answers):
    letters = ["a","b","c","d"]
    for i in range (len(answers)):
        print(letters[i]+": "+answers[i])

#Choose a letter => Choose a value in the answers array
# a=0,b=1,c=2,d=3
#"input" is a number 
# number is the nth question
def verif(number, correct_answers, incorrect_answers, answers, choice):
    correct = False

    if(answers[choice]==correct_answers[number]):
        correct = True
    return correct


points = 0
for i in range (amount):

    print("Points : "+str(points) + "\n")
    question(i,categories,questions,correct_answers,incorrect_answers,difficulties)
    print("\n")
    answ = shuffleAnswers(i,correct_answers,incorrect_answers)
    showQuestions(answ)
    print("\n")
    playerChoice = input("Your choice (type a letter)>")
    if(playerChoice!='a' and playerChoice!='b' and playerChoice!='c' and playerChoice!='d'):
        while(playerChoice!='a' and playerChoice!='b' and playerChoice!='c' and playerChoice!='d'):
            print("Wrong input, try again.")
            playerChoice = input("Your choice (type a letter)>")
    choiceValue = 0
    if(playerChoice=='b'):
        choiceValue = 1
    elif(playerChoice=='c'):
        choiceValue = 2
    elif(playerChoice=='d'):
        choiceValue = 3
    
    if(verif(i, correct_answers,incorrect_answers,answ,choiceValue)):
        print("Correct !\n")
        points+=1
    else:
        print("Wrong, the correct answer was "+correct_answers[i]+ "\n")
    
    print("========================================================================================================")
print("There are no longer questions. You got "+points +" points")