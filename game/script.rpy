# Importa el archivo con las definiciones de las pantallas
$ renpy.include("screens.rpy")

init python:
    import random

# Define las imágenes que se utilizarán
image bg sala = "sala.jpg"

# Inicio de la historia
label start:
    scene bg sala

    "You are BMO, a small game console with a thirst for adventure."
    
    "Eileen: Hello, BMO! Ready to play rock, paper, or scissors?"

    $ score_player = 0
    $ score_computer = 0
    $ choices = ['Rock', 'Paper', 'Scissors']

    while score_player < 3 and score_computer < 3:
        "Scores: BMO - [score_player] | Eileen - [score_computer]"

        $ player_choice = renpy.input("What do you choose? (Rock/Paper/Scissors)").strip().capitalize()

        if player_choice not in choices:
            "Please choose 'Rock', 'Paper', or 'Scissors'."
        else:
            $ computer_choice_index = random.randint(0, 2)
            $ computer_choice = choices[computer_choice_index]
            "You choose [player_choice]. Eileen chooses [computer_choice]."

            if player_choice == computer_choice:
                "It's a tie!"
            elif (player_choice == 'Rock' and computer_choice == 'Scissors') or (player_choice == 'Paper' and computer_choice == 'Rock') or (player_choice == 'Scissors' and computer_choice == 'Paper'):
                "You win the game!"
                $ score_player += 1
            else:
                "Eileen wins the game."
                $ score_computer += 1

    if score_player == 3:
        "You won the match! Well done, BMO!"
    else:
        "Eileen won the match. Better luck next time, BMO!"

    return
