import random
num = random.randint(1, 100)
lives = 5
print("u have 5 lives, guess a number between 1 - 100")

while lives > 0:
    guess = int(input())
    if guess > num:
        lives -= 1
        print(f"try a smaller number, u have {lives} lives left")
    elif guess < num:
        lives -= 1
        print(f"try a bigger number, u have {lives} lives left")
    else:
        print("THAT WAS CORRECT!")
        break
if lives==0:
    print(f"u failed!, the number was {num}")
else:
    print(f"u took {5 - lives} lives to guess it")
