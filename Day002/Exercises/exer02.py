#Write your code below this line 👇

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# print(type(height))
# print(type(weight))

new_height = int(height)
new_weight = float(weight)

bmi = (new_weight) / (new_height**2)

new_bmi = int(bmi)

print(new_bmi)