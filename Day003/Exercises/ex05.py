#Write your code below this line 👇

print("Welcome to  the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name = name1 + name2
true = name.count('t') + name.count('r') + name.count('u') + name.count('e')
love = name.count('l') + name.count('o') + name.count('v') + name.count('e')

score = int(f'{true}{love}')

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 < score < 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')