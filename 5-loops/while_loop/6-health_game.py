import random

# initialize the game
player_health = 100
enemy_health = 100
player_name = input("Enter your name: ")
print(f"Welcome to the game, {player_name}!")

# start the game loop
while player_health > 0 and enemy_health > 0:
    # get the player's move
    print(f"Your health: {player_health}")  # format specifyer as f""
    print("Enemy health: {}".format(enemy_health))  # or .format() are all the same
    move = input("Enter your move (1: attack, 2: heal): ")

    # execute the player's move
    if move == "1":
        damage = random.randint(10, 20)
        enemy_health -= damage
        print("You attack the enemy for {} damage!".format(damage))
    elif move == "2":
        heal = random.randint(5, 10)
        player_health += heal
        print("You heal yourself for {} health!".format(heal))
    else:
        print("Invalid move, try again.")

    # check if the game is over
    if enemy_health <= 0:
        print("You win!")
        break

    # execute the enemy's move
    enemy_move = random.randint(1, 2)
    if enemy_move == 1:
        damage = random.randint(10, 20)
        player_health -= damage
        print("The enemy attacks you for {} damage!".format(damage))
    elif enemy_move == 2:
        heal = random.randint(5, 10)
        enemy_health += heal
        print("The enemy heals for {} health!".format(heal))

    # check if the game is over
    if player_health <= 0:
        print("You lose!")
        break

# end the game
print("Thanks for playing!")
