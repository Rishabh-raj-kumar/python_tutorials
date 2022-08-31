def new_game():
    guesses=[]
    correctGuess=0
    quesNum=1

    for k in questions:
        print("---------------------------------")
        print (k)
        for i in options[quesNum-1]: #to print each option for specifid question
            print(i)

        guess=input("Enter you choice (A,B,C,D) : ");
        guesses.append(guess)

        correctGuess+= check_ans(questions.get(k),guess) #increment correct guess by 1 after each iteration
        quesNum+=1  #to change option after every iteration

        display_score(correctGuess,guesses) #show user final result

def check_ans(ans,guess):
    if ans == guess:
        print("Correct");
        return 1
    else:
        print("Not Correct")
        return 0

def display_score(correct,guesses):
    print("Answers : ")
    print("----------------------")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    for i in guesses:
        print(i,end=" ")
    print()

    score=int(correct/len(questions)*100)
    print("Your Score is : {} %".format(score))

def play_again():
    responce = input("Do you want to play again : (yes or no)")
    responce = responce.upper()

    if(responce == "YES"):
     return True
    else:
        return False


questions={"where is your home : ":"A",
           "where are your homies : ":"B",
           "where is tarbine : ":"C"}

options = [["A.shimla","B.china","C.chennai","D.Ranchi"],
           [ "A.patna","B.udisa","C.chaksi","D.repso"],
           [ "A.vsCode","B.intellij","C.fibre","D.depra"]]

new_game()

while play_again():
    new_game()

print ("BYeeeee")  #if user exists