import random

def find_winner(user_c, computer_c):
    if (
            (user_c == "Schere" and computer_c == "Papier") or
            (user_c == "Papier" and computer_c == "Stein") or
            (user_c == "Stein" and computer_c == "Schere")
    ):
        return "Du gewinnst!"
    elif user_c == computer_c:
        return "Egal!"
    else:
        return "Der Computer gewinnt!"


def load_file():
    file = open("../zeichen.txt", 'r')
    zeichen = file.read().split('\n\n')
    return zeichen

def print_zeichen(zeichen, idx):
    print(zeichen[idx])
