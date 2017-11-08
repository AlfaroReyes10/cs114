import random

print("Welcome To Space Dungeon Part II")
print("Your Journey Begins Now!")

magic_points = 50
hit_points = 50

while(magic_points > 0) == True:
    print(" You have",magic_points,"magic points")
    print("you cast a spell")
    magic_points -= random.randint(1,50)

# print("You have casted a spell")

for attack in range(5):
    damage = random.randint(1,50)
    print(hit_points)
    hit_points -= damage
    if hit_points == 0:
        print("you died")
