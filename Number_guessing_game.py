import random
high_score = None
print()
print("----------NUMBER GUESSING GAME--------")
print()

while True:

    print("\nEnter the difficulty:")
    print("1. Easy(1-50)")
    print("2. Moderate(1-100)")
    print("3. High (1-200)") 

    print()

    while True:

        Diff = input("Enter the difficulty among 1,2 or 3")
     
        print()

        if Diff == "1":
            number = random.randint(1,50)
        elif Diff == "2":
            number = random.randint(1,100)
        elif Diff == "3":
            number = random.randint(1,200)
        else:
            print("Choose a difficulty among 1,2 or 3\n")
            break

        attempt = 0

        while True:
            try:
                guess = int(input("Enter the number"))
            except ValueError:
                print("Please enter a valid number!")
                attempt += 1


            if 0< guess-number <10:
                print("Closely High")
            elif 0< number-guess <10:
                print("Closely Low")
            elif 10< guess-number <30:
                print("High")
            elif 10< number-guess <30:
                print("Low")
            elif guess-number>30:
                print("Too High")
            elif number-guess>30:
                print("Too Low")

            if guess == number:
                print(f"\nCorrect! You have guessed the number in {attempt} tries")

                if high_score is None or high_score>attempt:
                    high_score= attempt
                    print("New High Score")

                break

            elif attempt == 10:
                print(f"Out of attempt! The number was {number}")

                break

            

        

        print()

        print(f"Your current high score is {high_score}:")

    

        again = input("Do you wanna play again:(Yes/No)")
        if again.lower() == "no":
            break