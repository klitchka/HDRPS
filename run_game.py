import random
from web3 import Web3
from mantle import Mantle, ContractService, KeystoreService, mantledragon

# Conexión a la red Ethereum
provider_url = "https://linea-goerli.infura.io/v3/548c4b2405cf468dac18562921b3e425"
provider = mantledragon.providers.InfuraProvider("rinkeby", provider_url)

# Carga el contrato inteligente desde el archivo compilado (ABI y bytecode)
contract_abi = open("contract_abi.json", "r").read()
contract_bytecode = open("contract_bytecode.txt", "r").read()

# Crea una instancia del contrato
contract = mantledragon.Contract(contract_abi, contract_bytecode, provider)

# Define las opciones del juego
choices = ['Rock', 'Paper', 'Scissors']

# Función para obtener la elección del jugador
def get_player_choice():
    while True:
        player_choice = input("What do you choose? (Rock/Paper/Scissors): ").strip().capitalize()
        if player_choice in choices:
            return player_choice
        else:
            print("Please choose 'Rock', 'Paper', or 'Scissors'.")

# Función para obtener la elección de la computadora
def get_computer_choice():
    return random.choice(choices)

# Función para determinar el ganador del juego
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or (player_choice == 'Paper' and computer_choice == 'Rock') or (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win the game!"
    else:
        return "Computer wins the game."

# Inicio del juego
def play_game():
    score_player = 0
    score_computer = 0

    while score_player < 3 and score_computer < 3:
        print("Scores: Player - {} | Computer - {}".format(score_player, score_computer))

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print("You choose {}. Computer chooses {}.".format(player_choice, computer_choice))

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win the game!":
            score_player += 1
        elif result == "Computer wins the game.":
            score_computer += 1

    if score_player == 3:
        print("Congratulations! You won the match!")
    else:
        print("Computer won the match. Better luck next time.")

# Inicia el juego
play_game()
