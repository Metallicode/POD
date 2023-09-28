import random

class Player:
    def __init__(self):
        self.health = 100
        self.score = 0
        self.inventory = []
        self.strength = 20

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def add_score(self, points):
        self.score += points

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            if item == "Food":
                print("You ate some food and recovered some health.")
                self.heal(20)
            elif item == "Medicine":
                print("You used some medicine and recovered a lot of health.")
                self.heal(50)
            elif item == "Weapon":
                return self.strength
        return 0

class Enemy:
    def __init__(self):
        self.health = random.randint(50, 100)
        self.strength = random.randint(5, 15)

    def attack(self):
        return self.strength




def generate_path(steps):
    return [random.choice(['passage', 'battle', 'rest', 'item']) for _ in range(steps)]

def initiate_battle(player):
    enemy = Enemy()
    while player.health > 0 and enemy.health > 0:
        action = input("Choose an action: (hit head/body/legs, defend, medicine): ").strip().lower()
        enemy_damage = enemy.attack()

        if action == "defend":
            player.take_damage(enemy_damage // 2)
            print(f"Defended! Took {enemy_damage // 2} damage.")
        elif action == "medicine":
            if "Medicine" in player.inventory:
                player.use_item("Medicine") 
            else:
                print("You have no medicine...")
        else:
            if action == "head":
                enemy.health -= random.randint(5, 30) + player.use_item("Weapon")
            elif action == "body":
                enemy.health -= random.randint(1, 20) + player.use_item("Weapon")
            elif action == "legs":
                enemy.health -= random.randint(5, 15) + player.use_item("Weapon")
            player.take_damage(enemy_damage)
            print(f"Took {enemy_damage} damage.")
            print(f"Player health {player.health*'*'}")
            print(f"Enemy health {enemy.health*'*'}")

    if enemy.health <= 0:
        print("Enemy defeated!")
        player.add_score(10)
    else:
        print("You were defeated!")

def game_loop(player, path):
    for step in path:
        if step == "passage":
            print("You continue on your journey...")
        elif step == "battle":
            print("You encounter an enemy!")
            initiate_battle(player)
            if player.health == 0:
                break
        elif step == "rest":
            print("You find a place to rest and recover some health.")
            player.heal(5)
            if "Food" in player.inventory:
                user_choice = input("Use Food? (yes/no): ").strip().lower()
                if user_choice == "yes":
                    player.use_item("Food")
        elif step == "item":
            item = random.choice(["Food", "Medicine", "Weapon"])
            print(f"You found {item}!")
            player.add_item(item)
        input("Press Enter to continue to the next step...")

    end_game(player)

def end_game(player):
    print(f"Game Over! Your score is: {player.score}")
    replay = input("Play again? (yes/no): ").strip().lower()
    if replay == "yes":
        main()




def main():
    intro_msg = '''Welcome to "Path of Destiny"!

In this mystical journey, you are an adventurer embarking on an unknown path fraught with challenges and rewards. Each step you take can lead to one of four possible scenarios:

Passage: A simple step forward on your journey.
Battle: An encounter with a formidable enemy. During battle, you have the choice to target the enemy's head, body, or legs. Different attacks have varied damage outputs, but beware! The enemy also seeks to defeat you.
Rest: A moment of respite where you can recover some health.
Item: Discoveries of beneficial items that can aid you. Items include:
Food: Restores a portion of your health.
Medicine: Restores a large portion of your health.
Weapon: Temporarily increases your damage output in the next attack.
Your main objective is to reach the end of the path and achieve the highest score. Your score increases by overcoming battles and based on how efficiently you handle encounters. Remember to manage your health and use your items wisely.

Let the journey begin, and may the "Path of Destiny" favor you!
    '''
    print(intro_msg)
    input("Press Any Key To Start Game!")
    player = Player()
    path = generate_path(10)
    game_loop(player, path)

if __name__ == "__main__":
    main()
