

def newGame():
    guesses=[]
    correctGuesses=0
    questionNum=1
    
    for key in qna:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(key)
        for i in options[questionNum-1]:
            print(i)
        guess = input("Please enter (A B C D) :").upper()
        guesses.append(guess)
        
        correctGuesses += checkAnswer(qna.get(key), guess)
        questionNum+=1
    displayScore(correctGuesses,questionNum)
    play_again()
        
        
def checkAnswer(answer, guess):
    if answer == guess:
        print("Yay, this is Correct")
        return 1
    else: 
        print("Whopps, this seems wrong")
        return 0
    
def displayScore(correct,total):
    percent=(correct/(total-1))*100
    print(f"\nGood game! out of {total-1} questions you got {correct}")
    print(f"You got {percent}%")
    
def play_again():
    play_again=input("Would you like to play again (Yes/No) : ").lower()    
    if(play_again)=="yes":
        newGame()
    else:
        print("\nHope you had fun, Good bye!")

qna={
    "dummy question, answer is A":"A",
    "dummy question, answer is B":"B",
    "dummy question, answer is C":"C",
    "dummy question, answer is D":"D",
}

options=[
    ["A. Right","B. Wrong","C. Wrong","D. Wrong"],
    ["A. Wrong","B. Right","C. Wrong","D. Wrong"],
    ["A. Wrong","B. Wrong","C. Right","D. Wrong"],
    ["A. Wrong","B. Wrong","C. Wrong","D. Right"]
    
]

newGame()
