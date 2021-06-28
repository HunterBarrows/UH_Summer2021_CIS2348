# Hunter Barrows    1550107

# Zylab 11.27

# Set up roster
def Roster():
    list_player = list(players.keys())
    list_player.sort()

    print("ROSTER")
    for player in list_player:
        print("Jersey number: {}, Rating: {}".format(player, players[player]))

players = {}

# get user input to gert jersey number and rating

for i in range(0, 5):
    jersey = int(input("Enter player %d's jersey number:\n" % (i + 1)))
    players[jersey] = int(input("Enter player %d's rating:\n" % (i + 1)))
    print("")

Roster()

# set up menu with options for user
while True:
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")

    option = input("Choose an option:\n")

    if option == "q":
        break

    if option == 'o':
        Roster()

    elif option == 'a':
        jersey = int(input("Enter a new player's jersey number: \n"))
        rate = int(input("Enter the player's rating:\n"))
        players[jersey] = rate

    elif option == 'd':
        jersey = int(input("Enter a player's jersey number: \n"))
        if jersey in list(players.keys()):
            del players[jersey]

    elif option == 'u':
        jersey = int(input("Enter a player's jersey number: \n"))
        rate = int(input("Enter a new rating for player:\n"))
        players[jersey] = rate

    elif option == 'r':
        rate = int(input("Enter a rating:\n"))
        player = list(players.keys())
        player.sort()
        print("\nABOVE {}".format(rate))

        count = 0
        for i in player:
            if (players[i] > rate):
                print("Jersey number: %d, Rating: %d" % (i, players[i]))
                count += 1
        if (count == 0):
            print("No players found above %d rating" % (rate))
    if option == "q":
        break


