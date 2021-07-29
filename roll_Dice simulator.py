import random

# The computer rolls a random number between 1 to 6
comp_roll = random.randint(1,6)


user_roll = input("Press y to roll the dice !!:\t")

# The user press 'y', which generated a similar random number between 1 to 6.

if user_roll == "y":
	user_roll = random.randint(1,6)

# The user gets to see both of the results.

print(f"The computer rolled {comp_roll}.\n")
print(f"You rolled {user_roll}.\n")

# The final result is shown to the user in the form of win/lose/draw.

if comp_roll > user_roll:
	print("You lost. Nice try though !!\n")
elif user_roll > comp_roll:
	print("You won !!\n")
elif user_roll == comp_roll:
	print("Its a draw! That sucks.\n")

print("Thank you for playing!!")