import random
import sys

print(" WELCOME THE BATTLE OF THE CENTURY!")
print("The princess of Venice has been kidnapped by the 3 Demons of hell. It is your job to defeat them all in order to save her and bring her back to her thrown.")
print("Choose your character wisely...")
print("Select A character" )
print("Dwarf")
print("Giant")
print("Knight")
print("SwordsMen")
print("Warrior")
character = input()
print('You have chosen,' + character)
print('Your Journey will begin now are you ready!!')


player = {
'HP': 100,
'attack': 100,
'defense': 100,
'magic':100,
'name': character
}

enemy1 = {
'HP': 100,
'attack': 100,
'defense': 100,
'Special_Power':400,
'name': 'The Demon King'
}

enemy2 = {
'HP': 80,
'attack': 80,
'defense': 80,
'name': 'Demon Gallows'
}

enemy3 = {
'HP': 60,
'attack': 60,
'defense': 60,
'name': 'Demon Finn Balor '
}

def game_over(player):
    print("GAME OVER -- ", player['name'],
    "You have failed to save the princess.")
    return sys.exit()


def get_item(player):
    item_list = ["MRE", "magic potion that has increased your HP",]

    print("You find a ", item_list[random.randint(0, 2)], "your health increased by ",
    (abs(player['HP'] - 100)), "HP")
    player['HP'] += (abs(player['HP'] - 100))
    return player

def attack(opponent):
    rand_damage = random.randint(8, 32)
    opponent['HP'] -= rand_damage
    print(rand_damage, " damage!")
    return opponent


def fight(oppo1, oppo2):
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0):
        print(oppo1['name'], " attacks ", oppo2['name'])
        attack(oppo2)
        if oppo2['HP'] <= 0:
            print(oppo1['name'], " is winner")
        else:
            print(oppo2['name'], " attacks ", oppo1['name'])
            attack(oppo1)
        if oppo1['HP'] <= 0:
            print(oppo2['name'], " is winner")
            game_over(oppo1)
    print(character +  'oppo1 HP: ', oppo1['HP'])
    print('enemy1  oppo2 HP: ', oppo2['HP'])


def encounter(player, opponent):
    if player['HP'] > 70:
        fight(player, opponent)
        # if player['HP'] <= 0:
        #     return game_over(player)
        input('Press any key to continue')
    elif opponent['name'] == 'The Demon King':
        fight(player, opponent)
        # return player
    else:
        get_item(player)
        input('Press any key to continue')


def main():
    # fight(player, enemy1)

    # get_item(player)
    print('encounter 1...\n\n')
    encounter(player, enemy3)
    print('encounter 2...\n\n')
    encounter(player, enemy2)
    print('encounter 3...\n\n')
    encounter(player, enemy1)
    print("YOU HAVE SAVED THE PRINCESS -- MISSION COMPLETE", player['name'], " HP: ", player['HP'])


if __name__ == "__main__":
    # print("Executing as main program")
    # print("Value of __name__ is: ", __name__)
    main()
