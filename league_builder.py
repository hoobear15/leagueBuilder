import csv

def main():

    #load player file with data
    player_data = import_players()

    #build teams with player data
    teams = build_teams(player_data)

    #print teams to file
    file_print(teams)

    #create welcome letters to all players
    letter_builder(teams)

def import_players():

    #load csv file
    with open('soccer_players.csv') as csvfile:
        #read the csv file to a dictionary (will use first row as keys in dict)
        players = csv.DictReader(csvfile)
        # put in python object
        rows = list(players)

    #return list of players
    return rows

def build_teams(players):

    #create teams
    dragons = []
    sharks = []
    raptors = []

    #get experienced players and new players in separate lists
    experienced_players = []
    new_players = []
    for each in players:
        if each['Soccer Experience'] == 'YES':
            experienced_players.append(each)
        else:
            new_players.append(each)

    #disburse players
    #experienced players
    num_explayers = len(experienced_players)
    players_team = int(num_explayers/3)

    for player in range(0,players_team):
        dragons.append(experienced_players.pop())
        sharks.append(experienced_players.pop())
        raptors.append(experienced_players.pop())

    #new players
    num_newplayers = len(new_players)
    players_team = int(num_newplayers / 3)

    for player in range(0, players_team):
        dragons.append(new_players.pop())
        sharks.append(new_players.pop())
        raptors.append(new_players.pop())

    return {"Dragons":dragons,"Sharks":sharks,"Raptors":raptors}

def file_print(teams):

    #open new file to place teams
    with open('teams.txt','a') as source_file:

        for team in teams:
            source_file.write(team + '\n')
            for player in teams[team]:
                line = player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n'
                source_file.write(line)
            source_file.write('\n')

def letter_builder(teams):

    #loop through each player, by team, to create letters
    for team in teams:
        for player in teams[team]:

            #build the file name
            file_name = str(player['Name'].lower()).replace(' ','_') + '.txt'

            #open and print info to file
            with open(file_name, 'a') as source_file:
                line = 'Dear ' + player['Guardian Name(s)'] + ',\n\n' + 'Welcome to our league! We wanted to inform you that ' + \
                player['Name'] + ' will be playing with the ' + team + ' this year.\n\nOur first league wide practice will take place next week Friday.'
                source_file.write(line)

if __name__ == "__main__":
    main()
