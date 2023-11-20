from dice import Dice
def main():
    dice = Dice(6)
    while True:
        number = dice.throw()
        if number == 6:
            print("You win! You rolled 6")
            break
        else:
            print("You didn't win, you rolled ", number)


main()