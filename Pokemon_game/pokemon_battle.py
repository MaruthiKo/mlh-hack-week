import requests 
import random

class Pokemon:
    def __init__(self, name, base_experience, height):
        self.name = name
        self.base_experience = base_experience
        self.height = height

    def display_details(self):
        print(f"{self.name} - Base Experience: {self.base_experience} - Height: {self.height}")

def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Pokemon(data['name'], data['base_experience'], data['height'] / 10)  # Convert height to meters
    else:
        print(f'Error fetching {pokemon_name} data. Try again.')
        return None


def main():
    print('Welcome to Pokémon Battle Simulator!')

    player_choice = input("Enter the name of your Pokémon: ").capitalize()
    player_pokemon = get_pokemon_data(player_choice)

    if not player_pokemon:
        return

    # The computer's Pokémon (you can add more Pokémon here)
    computer_pokemon = get_random_pokemon()

    # The main battle loop
    while player_pokemon.base_experience > 0 and computer_pokemon.base_experience > 0:
        # Display the Pokémon details before each turn
        print("\nPlayer's Turn:")
        player_pokemon.display_details()
        print("\nComputer's Turn:")
        computer_pokemon.display_details()

        # Determine the winner of each round
        if player_pokemon.base_experience > computer_pokemon.base_experience:
            print(f"\n{player_pokemon.name} wins this round!")
            computer_pokemon.base_experience = 0
        elif player_pokemon.base_experience < computer_pokemon.base_experience:
            print(f"\n{computer_pokemon.name} wins this round!")
            player_pokemon.base_experience = 0
        else:
            print("\nIt's a tie!")

    # Determine the overall winner of the battle
    if player_pokemon.base_experience > 0:
        print(f"\n{player_pokemon.name} wins the battle!")
    elif computer_pokemon.base_experience > 0:
        print(f"\n{computer_pokemon.name} wins the battle!")
    else:
        print("\nIt's a tie!")

def get_random_pokemon():
    pokemon_id = random.randint(1, 898)  # There are 898 Pokémon in the Pokédex
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Pokemon(data['name'], data['base_experience'], data['height'] / 10)  # Convert height to meters
    else:
        print('Error fetching Pokémon data. Try again.')
        return None

if __name__ == "__main__":
    main()

