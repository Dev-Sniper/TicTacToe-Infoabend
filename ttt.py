from random import randint


#Author: Dev_Sniper
#©Dev_Sniper 2021


field_array = [[" ", "A", "B", "C"], ["1", "-", "-", "-"], ["2", "-", "-", "-"], ["3", "-", "-", "-"]]
pcsymbol1 = "X"
pcsymbol2 = "O"

def print_field():
    for row in field_array:
        if row[0] != " ":
            print("------------------")
        print("|", row[0], "|", row[1], "|", row[2], "|", row[3], "|")

print_field()
print("------------------")
Usymbol = input("Welches Symbol willst du nutzen? ")
mode = input("Gegen den Computer (C) oder gegen eine andere Person (P) spielen?").lower()
if mode == "p":
    Usymbol2 = input("Zweiter Spieler spielt mit: ")
if mode != "p" and mode != "c":
    exit()

def UInput():
    col = input("Gib die Spalte an (oder beende das Spiel mit stop, break oder s: ").lower()
    if col == "stop" or col == "break" or col == "s":
        exit()
    if col != "a" and col != "b" and col != "c":
        UInput()
    row = input("Gib die Zeile ein: ")
    if row != "1" and row != "2" and row != "3":
        UInput()
    checkUInput(col, row)

def checkUInput(col, row):
    if col == "a":
        xcord = 1
    elif col == "b":
        xcord = 2
    elif col == "c":
        xcord = 3
    if row == "1":
        ycord = 1
    elif row == "2":
        ycord = 2
    elif row == "3":
        ycord = 3
    setUMove(xcord, ycord)

def setUMove(xcord, ycord):
    if field_array[ycord][xcord] == "-":
        field_array[ycord][xcord] = Usymbol
    else:
        print("Ungültige Eingabe")
        UInput()
    checkWin()
    if mode == "p":
        UInput()
    elif mode == "c":
        PCMove()

def PCMove():
    randx = randint(1, 3)
    randy = randint(1, 3)
    if field_array[randy][randx] == "-":
        if pcsymbol1 != Usymbol:
            field_array[randy][randx] = pcsymbol1
        else:
            field_array[randy][randx] = pcsymbol2
    else:
        PCMove()
    checkWin()
    print_field()
    UInput()

def checkWin():
    x = 1
    y = 1
    while y <= 3:
        if field_array[y][x] == field_array[y][x+1] and field_array[y][x] == field_array[y][x+2] and field_array[y][x] != "-":
            if mode == "c":
                if Usymbol == field_array[y][x]:
                    print("Du gewinnst!")
                else:
                    print("Du hast verloren!")
            else:
                if Usymbol == field_array[y][x]:
                    print("Spieler 1 gewinnt!")
                else:
                    print("Spieler 2 gewinnt!")
            print_field()
            replay = input("Neues Spiel (J/N)?\n").lower()
            if replay == "j":
                print("Starte neues Spiel")
                game_replay()
            else:
                exit()
        y += 1
    y = 1

    while x <= 3:
        if field_array[y][x] == field_array[y+1][x] and field_array[y][x] == field_array[y+2][x] and field_array[y][x] != "-":
            if mode == "c":
                if Usymbol == field_array[y][x]:
                    print("Du gewinnst!")
                else:
                    print("Du hast verloren!")
            else:
                if Usymbol == field_array[y][x]:
                    print("Spieler 1 gewinnt!")
                else:
                    print("Spieler 2 gewinnt!")
            print_field()
            replay = input("Neues Spiel (J/N)?\n").lower()
            if replay == "j":
                print("Starte neues Spiel")
                game_replay()
            else:
                exit()
        x += 1
    x = 1

    if field_array[1][1] == field_array[2][2] and field_array[1][1] == field_array[3][3] and field_array[1][1] != "-":
        if mode == "c":
            if Usymbol == field_array[1][1]:
                print("Du gewinnst!")
            else:
                print("Du hast verloren!")
        else:
            if Usymbol == field_array[1][1]:
                print("Spieler 1 gewinnt!")
            else:
                print("Spieler 2 gewinnt!")
        print_field()
        replay = input("Neues Spiel (J/N)?\n").lower()
        if replay == "j":
            print("Starte neues Spiel")
            game_replay()
        else:
            exit()
    if field_array[1][3] == field_array[2][2] and field_array[1][3] == field_array[3][1] and field_array[1][3] != "-":
        if mode == "c":
            if Usymbol == field_array[1][3]:
                print("Du gewinnst!")
            else:
                print("Du hast verloren!")
        else:
            if Usymbol == field_array[1][3]:
                print("Spieler 1 gewinnt!")
            else:
                print("Spieler 2 gewinnt!")
        print_field()
        replay = input("Neues Spiel (J/N)?\n").lower()
        if replay == "j":
            print("Starte neues Spiel")
            game_replay()
        else:
            exit()
    check_stalemate()

def check_stalemate():
    if field_array[1][1] != "-" and field_array[1][2] != "-" and field_array[1][3] != "-" and field_array[2][1] != "-" and field_array[2][2] != "-" and field_array[2][3] != "-" and field_array[3][1] != "-" and field_array[3][2] != "-" and field_array[3][3] != "-":
        print("Unentschieden!")
        replay = input("Neues Spiel (J/N)?\n").lower()
        if replay == "j":
            print("Starte neues Spiel")
            game_replay()
        else:
            exit()

def game_replay():
    x = 1
    y = 1
    while x <= 3:
        while y <= 3:
            field_array[y][x] = "-"
            y += 1
        y = 1
        x += 1
    x = 1
    print_field()
    UInput()

UInput()