#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = (tip / 100) * bill + bill

valor = (bill_with_tip / people)

final_valor = round(valor, 2)

final_valor = "{:.2f}".format(final_valor)

message = f"Each person should pay: ${final_valor}"
print(message)  