from functions import find_winner
def test_find_winner ():
    assert find_winner("Schere", "Papier") == "Du gewinnst!"
    assert find_winner("Schere", "Stein") == "Der Computer gewinnt!"
    assert find_winner("Stein", "Stein") == "Egal!"