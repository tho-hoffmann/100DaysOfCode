#Write your code below this row 👇

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        # Divisble by both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:
        # Divisble by 3
        print("Fizz")
    elif number % 5 == 0:
        # Divisble by 5
        print("Buzz")
    else:
        print(number)