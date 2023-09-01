import random
number = random.randint(1,100)
lives = 0
difficulty = input("Choose your difficulty 1 for easy 2 for medium 3 for hard ")

def easy():
        return lives + 10

def medium():
        return lives + 5

def hard():
        return lives + 3

if difficulty == "1":
    lives = easy()

if difficulty == "2":
    lives = medium()

if difficulty == "3":
    lives = hard()

while lives != 0:
    guess = int(input("What is your guess? "))
    if guess > number:
        lives -= 1
        print(f"lower your life is now {lives}")
    elif guess < number:
        lives -= 1
        print(f"higher your life is now {lives}")
    elif guess == number:
        print("You win")
        break