import random
Random=random.randint(1,10)
Guess_Number=int(input("Enter a number between 1 to 10: "))
if Guess_Number==Random:
    print("Congratulation! you guess correct number!")
elif Guess_Number<Random:
    print("It's too low! try again.")
else:
    print("It's too High! try again.")