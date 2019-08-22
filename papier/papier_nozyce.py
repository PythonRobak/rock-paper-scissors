import random

name = input("Jak masz na imię? :")

def welcome_message():
    print("Cześć " + name + "!")
    print("Zagrajmy w papier, nożyce, kamień.")


def player_decision():
    print("Co wybierasz?")
    print("1 - Papier")
    print("2 - Nożyce")
    print("3 - Kamień")
    player_input = input("Na co się decydujesz?: ")
    if int(player_input) != 1 and int(player_input) != 2 and int(player_input) != 3:
        print("W kulki sobie lecisz? Wprowadź poprawną wartość!")
    else:
        if int(player_input) == 1:
            print("Wybrałeś Papier")
        elif int(player_input) == 2:
            print("Wybrałeś Nożyce")
        elif int(player_input) == 3:
            print("Wybrałeś Kamień")
        else:
            print("W kulki sobie lecisz? Wprowadź poprawną wartość!")

    return int(player_input)


def computer_decision():
    input_kompa = random.randint(1, 3)
    if input_kompa == 1:
        str_input_kompa = "Papier"
    elif input_kompa == 2:
        str_input_kompa = "Nożyce"
    else:
        str_input_kompa = "Kamień"

    print("Ja wybrałem " + str_input_kompa)
    return int(input_kompa)

def game():
    print("*"*50)
    print("Zaczynamy grę")
    print("*" * 50)
    print("")

    a = player_decision()
    b = computer_decision()


    if a == 1 and b == 1:
        print("Mamy remis! Musimy zagrać jeszcze raz!")
        game()
    elif a == 1 and b == 2:
        print("Wygrałem! Moje nożyce tną Twój papier, mam nadzieję, że nie jest Ci smutno!")
    elif a == 1 and b == 3:
        print("Wygrałeś! Twój papier owija mój kamień. Gratuluję!")
    elif a == 2 and b == 1:
        print("Wygrałeś! Nożyce tną papier - ciach ciach ciach!")
    elif a == 2 and b == 2:
        print("Mamy remis! Musimy zagrać jeszcze raz!")
        game()
    elif a == 2 and b == 3:
        print("Wygrałem! Nożyce tępią się na kamieniu!")
    elif a == 3 and b == 1:
        print("Wygrałem! Papier owija kamień!")
    elif a == 3 and b == 2:
        print("Wygrałeś! Twój kamień tępi moje nożyce!")
    elif a == 3 and b == 3:
        print("Mamy remis! Musimy zagrać jeszcze raz!")
        game()
    else:
        game()


welcome_message()
game()