import random
number = random.randint(0,100)
predict = 10
score = 0
guessNumber = 1

print("========= Number Guessing Game =========")
print("* You will try to guess a random number between 0-100.")
print("* For each wrong guess, 1 guess right is reduced, 5 guesses and 10 points are added for each correct guess.")
print("* You will be guided up or down according to your prediction.")
print("* Type '123' to exit.")
print(f"* Your right to predict: {predict}")

while predict > 0:
    guessInput = int(input(f"{guessNumber}. Guess: "))
    if guessInput == 123:
        print(f"You left, Your score: {score}")
        break
    if guessInput == number:
        predict += 5
        score += 10
        print(f"**You Guessed Correctly!! Your right to predict: {predict}**")
        print("*===============================*")
        guessNumber += 1
        number = random.randint(0,100)        
    else:
        predict -= 1
        guessNumber += 1
        print("*===============================*")
        print(f"Wrong guess, Your right to predict: {predict}")
        if guessInput < number:
            print("↑Up↑")
        else:
            print("↓Down↓")
    if predict < 1:
        print("*===============================*")
        print (f"You lost, Number held: {number}, Your score: {score}")
        break
