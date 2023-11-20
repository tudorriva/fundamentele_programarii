import random
from functions.functions import load_file, print_zeichen, find_winner


def main():
    zeichen = load_file()
    user_score = 0
    computer_score = 0

    for i in range(3):
        computer_c = random.choice(["Schere", "Stein", "Papier"])
        print("Computer hat gewählt!")
        user_c = input("Deine Wahl (Schere/Stein/Papier): ")

        if computer_c == "Schere":
            print_zeichen(zeichen, 2)
        elif computer_c == "Stein":
            print_zeichen(zeichen, 0)
        else:
            print_zeichen(zeichen, 1)

        if user_c == "Schere":
            print_zeichen(zeichen, 2)
        elif user_c == "Stein":
            print_zeichen(zeichen, 0)
        else:
            print_zeichen(zeichen, 1)

        print(f"Computer: {computer_c}")
        print(f"Du: {user_c}")

        result = find_winner(user_c, computer_c)
        if result == "Du gewinnst!":
            user_score = user_score + 1
        elif result == "Der Computer gewinnt!":
            computer_score = computer_score + 1
            print(result)

        print(f"Deine Punkte: {user_score}")
        print(f"Computer Punkte: {computer_score}")

    print("Spiel beendet!")
    if computer_score > user_score:
        print("Der Computer hat das Spiel gewonnen!")
    elif user_score > computer_score:
        print("Du hast das Spiel gewonnen!")
    else:
        print("Der Spiel hat sich Egal beendet.")



test_find_winner()
main()