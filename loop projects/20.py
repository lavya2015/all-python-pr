secret = 9
guess = 0

while guess != secret:
    guess = int(input("Enter number: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")

print("Correct!")