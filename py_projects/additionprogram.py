import random

randomNumber1 = random.randint( 20, 500 )
randomNumber2 = random.randint( 70, 1000 )
 

def askQuestion():
    global randomNumber1
    global randomNumber2

    userAnswer = int(input("What is " + str( randomNumber1 ) + " + " + \
                     str( randomNumber2 ) + " ? ") )
    return userAnswer

def checkAnswer( userAnswer ):
    global randomNumber1
    global randomNumber2

    correctAnswer = randomNumber1 + randomNumber2
    if userAnswer == correctAnswer:
        print("\nCongralutions Mo! You did a great job!")
    else:
        print("\nOops. That was close. The correct answer is ", correctAnswer)

def main():
    userAnswer = askQuestion()
    checkAnswer( userAnswer )

main()
