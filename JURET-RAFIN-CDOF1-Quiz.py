# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:52:05 2024

@author: MathisJuretRafin
"""

#We create the question according the following template : [Question, Proposition1, Proposition2, Proposition3, Proposition4, Answer]
#Each question has 4 propositions and one answer

question1 = ["What the capital city of France ?", "Paris", "Berlin", "Oslo", "Madrid", "Paris"]
question2 = ["What the capital city of Canada ?", "Ottawa", "Tokyo", "Sydney", "Mexico", "Ottawa"]
question3 = ["What the capital city of Ireland ?", "Bern", "Rome", "Dublin", "Berlin", "Dublin"]
question4 = ["What the capital city of China ?", "Beijing", "Tunis", "Brasilia", "Lisbon", "Beijing"]
question5 = ["What the capital city of Germany ?", "Paris", "Berlin", "Oslo", "Madrid", "Berlin"]

exit = False

while exit==False:
    #We initialize the score variable of our player
    score = 0

    #We create a list with all the questions
    questionList = [question1,question2,question3,question4,question5]

    #This method let the user have a better presentation of the questions
    def printQuestion(question):
        result = question[0] + "\n\n"
        for i in question[1:-1]:
            result += i + "\n"
        return result
    
  
    # This function checks if the user's answer is among the proposed answers
    def isAmongAnswers(question, answer):
        answer = answer.strip().lower()  # Remove leading and trailing whitespaces and convert to lowercase
        for i in question[1:-1]:
            if i.lower() == answer:  # Compare in lowercase
                return True
        return False

    # This section allows the user to answer the question
    for i in questionList:
        print("\n")
        print(printQuestion(i) + "\nEnter your answer :")
        answer = input()
        while not isAmongAnswers(i,answer):
            print("\nAnswer unknown ! Enter an answer among those proposed:")
            answer = input()
        if answer.strip().lower() == i[5].lower() : score += 1  # Compare in lowercase and ignore leading/trailing spaces
        print("\n")

    # This section displays the result with personalized comments
    if(score==0) : print("Your score is ", score, "... You should try to improve your culture")
    elif(score >0 and score <4) : print("Your score is ", score, ". You can do better !")
    elif(score == 4) : print("Your score is", score, "! Almost perfect !")
    else : print("Your score is ", score, "! Perfect !")

    rep = input('Enter r to restart or anything else to quit')
    if rep !='r':
        exit = True

print('End of the program')
        
    
    