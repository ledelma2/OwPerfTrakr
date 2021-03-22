#overwatch data retriever
#utilizes both the python-overwatch api and beautiful soup to retrive data
from overwatch import Overwatch

def getInfo(heroName, ow):
    data = []
    game = ow(mode="cp", hero=heroName, filter="game")
    i = game.index('Time Played')
    data.append(game[i+1])
    combat = ow(mode="cp", hero=heroName, filter="combat")
    i = combat.index('All Damage Done')
    data.append(combat[i+1])
    i = combat.index('Deaths')
    data.append(combat[i+1])
    i = combat.index('Eliminations')
    data.append(combat[i+1])
    i = combat.index('Objective Kills')
    data.append(combat[i+1])
    i = combat.index('Objective Time')
    data.append(combat[i+1])
    assists = ow(mode="cp", hero=heroName, filter="assists")
    return data

def main():
    overwatch = Overwatch(battletag="Serb#11472")
    print(getInfo('Zarya', overwatch))

if __name__ == '__main__':
    main()
