# Prompt the user to enter their score
score = float(input("Enter your score: "))

# Determine the performance level and calculate the amount of money
if score == 0.0:
    level = "Inaceptable"
    amount = 0
elif score == 0.4:
    level = "Aceptable"
    amount = 2400 * score
elif score >= 0.6:
    level = "Meritorio"
    amount = 2400 * score
else:
    level = "Invalid score"
    amount = 0

# Display the performance level and amount of money
print("Performance level:", level)
print("Amount of money:", amount)

