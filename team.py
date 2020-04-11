# TODO Create an empty list to maintain the player names
players = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
name_player = input("Quieres agregar jugadores a la lista? (Yes/No) :")

if name_player == "Yes":
    players.append(input("Escribe el nombre del jugador: "))
    ask = input("Quieres agregar más jugadores a la lista? (Yes/No) :")
    while ask == "Yes":
        players.append(input("Escribe el nombre del jugador: "))
        ask = input("Quieres agregar más jugadores a la lista? (Yes/No) :")

# TODO print the number of players on the team
print("Hay {} jugadores".format(len(players)))

# TODO Print the player number and the player name
# The player number should start at the number one
i = 0
while i<len(players):
    a = i+1
    print("El jugador {} corresponde a {}".format(a, players[i]))
    i += 1

# TODO Select a goalkeeper from the above roster
goalkeeper = int(input("Debes seleccionar al goalkeeper de la lista: "))

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("El goalkeeper es {}".format(players[goalkeeper-1]))
