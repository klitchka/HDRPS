# Pantalla de inicio
screen start_screen():
    vbox:
        text "Welcome to Rock, Paper, Scissors!"
        text "Press any key to start."
        key "start":
            jump start

# Pantalla de resultados
screen results_screen():
    vbox:
        text "Game Over"
        text "Final Score: BMO - [score_player] | Eileen - [score_computer]"
        textbutton "Play Again":
            jump start

# Pantalla principal del juego
screen game_screen():
    vbox:
        text "Scores: BMO - [score_player] | Eileen - [score_computer]"
        text "What do you choose? (Rock/Paper/Scissors)"
        input player_choice
        button "Submit":
            if player_choice in choices:
                jump resolve_turn

# Pantalla de resolución de turno
screen resolve_turn():
    vbox:
        text "You choose [player_choice]. Eileen chooses [computer_choice]."
        if player_choice == computer_choice:
            text "It's a tie!"
        elif (player_choice == 'Rock' and computer_choice == 'Scissors') or (player_choice == 'Paper' and computer_choice == 'Rock') or (player_choice == 'Scissors' and computer_choice == 'Paper'):
            text "You win the game!"
            $ score_player += 1
        else:
            text "Eileen wins the game."
            $ score_computer += 1
        if score_player < 3 and score_computer < 3:
            button "Continue":
                jump game_screen
        else:
            button "Continue":
                jump results_screen

# Pantalla de juego
screen game():
    add "sala.jpg"
    add game_screen()

# Pantalla de resultados
screen results():
    add "sala.jpg"
    add results_screen()

# Pantalla de inicio
screen start():
    add "sala.jpg"
    add start_screen()

# Inicia el juego en la pantalla de inicio
start()
