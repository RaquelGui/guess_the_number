#Guess the Number

# importing module
import random 


the_number = random.randint(1,100)  #range definition
guess_chances = 10  #number of tries
count = 1

print ("Let's play!")

while 1 <= guess_chances:
    guess = int(input ("Enter a number (1-100): "))

    if guess > the_number:
        print ("Too High. Guess a number lower than", guess)

    elif guess < the_number:
        print ("Too Low. Guess a number higher than", guess)

    else:
        print ("Congratulations! You win!")
        print (count, "attempts you've used")
        break

    guess_chances -= 1
    print (guess_chances, "chances left." )
    count += 1
    print ()

if guess_chances == 0:
    print("Game over!")
    print("The number is ", the_number)