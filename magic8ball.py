import random

print("This is a magic 8 ball program...")
print("Welcome what is your name? Afterwards please press enter to learn your fate.")
input()

random_num = random.randint(1, 9)

if random_num == 1:
    print("Today you will die")
elif random_num == 2:
    print("Today you will recieve a special surprise")
elif random_num == 3:
    print("You will win the lottery")
elif random_num == 4:
    print("You will fall off a cliff one day")
elif random_num == 5:
    print("You will recieve good news")
elif random_num == 6:
    print("YOU'VE WON")
elif random_num == 7:
    print("TRY AGAIN")
elif random_num == 8:
    print("Have Faith")
elif random_num == 9:
    print("You will find the love of your life today")
