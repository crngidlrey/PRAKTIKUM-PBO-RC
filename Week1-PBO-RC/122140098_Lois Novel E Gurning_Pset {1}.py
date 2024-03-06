import random

class Player:
    def __init__(self, name, available_heroes):
        self.name = name
        self.hp = 150
        self.available_heroes = available_heroes

    def choose_hero(self):
        print(f"{self.name}, choose your hero:")
        for i, hero in enumerate(self.available_heroes, start=1):
            print(f"{i}. {hero}")

        choice = int(input("Enter the number of your chosen hero (1-5): "))
        if 1 <= choice <= 5:
            self.hero = self.available_heroes.pop(choice - 1)
            print(f"{self.name} chose {self.hero} as their hero.")
        else:
            print("Invalid choice. Default hero selected.")
            self.hero = "DefaultHero"

    def attack(self, opponent):
        damage = random.randint(40, 60)
        if damage < 50:
            print(f"{self.hero}'s attack missed!")
            damage = random.randint(20, 30)

        opponent.receive_damage(damage)

    def regen(self):
        if self.hp < 10:
            self.hp += 50
            print(f"{self.hero} regenerated 50 HP.")
        else:
            print("Cannot regen at this time. HP is not low enough.")

    def give_up(self):
        print(f"{self.hero} gives up. {self.name} loses!")

    def receive_damage(self, damage):
        self.hp -= damage
        print(f"{self.hero} received {damage} damage. {self.hero}'s HP: {self.hp}")

class Game:
    def __init__(self):
        self.rounds = 1
        self.player1 = Player("Player 1", ["Yin", "Martis", "Badang", "Balmon", "Alpha"])
        self.player2 = Player("Player 2", ["Yin", "Martis", "Badang", "Balmon", "Alpha"])
        self.current_player = self.player1

    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def start_game(self):
        print("Welcome to Tera legend!")
        print("Five second to the enemy reaching the battle field")
        print("Smash them!")

        self.player1.choose_hero()
        self.player2.choose_hero()

        while True:
            print(f"\nRound {self.rounds}")
            print(f"{self.player1.hero}'s HP: {self.player1.hp} | {self.player2.hero}'s HP: {self.player2.hp}")

            print(f"\n{self.current_player.name}'s Turn:")
            if self.current_player == self.player1:
                print("1. Attack")
                print("2. Regen")
                print("3. Give Up")

                choice = int(input("Enter the number of your chosen action (1-3): "))

                if choice == 1:
                    self.current_player.attack(self.player2)
                elif choice == 2:
                    self.current_player.regen()
                elif choice == 3:
                    self.current_player.give_up()
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            else:
                ai_choice = random.randint(1, 3)
                if ai_choice == 1:
                    self.current_player.attack(self.player1)
                elif ai_choice == 2:
                    self.current_player.regen()
                else:
                    self.current_player.give_up()
                    break

            if self.player1.hp <= 0 or self.player2.hp <= 0:
                print("\nGame Over!")
                print(f"{self.current_player.name} wins!")
                break

            self.switch_turn()
            self.rounds += 1

if __name__ == "__main__":
    game_instance = Game()
    game_instance.start_game()