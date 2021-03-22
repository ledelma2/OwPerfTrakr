import json
from .enums import GameModes
from .lookups import dataTables, heroes

class OverwatchStatisticGenerator:
    """
    This class is for generating overwatch statistics.

    Attributes:
        overwatchUser (OverwatchUser): The user whose performance statistics are desired.
        gameMode (int): The gamemode for the desired stats.
    """

    def __init__(self, overwatchUser, mode = GameModes.QP):
        """
        Constructor for the OverwatchStatisticGenerator.
        Generates stats for quick play by default.

        Parameters:
            overwatchUser (OverwatchUser): The current overwatch user.
            mode (GameModes)(optional): Enum for the game mode desired.
        """
        self.overwatchUser = overwatchUser
        self.gameMode = 0 if mode == GameModes.QP else 1

    def GetHeroStatistics(self, hero) -> str:
        """
        Generates all statistics for a particular hero.

        Parameters:
            hero (Heroes): Enum for the hero desired.
        """
        heroStats = {}
        heroAddress = heroes[hero]
        css_selector = f'div[data-category-id="{heroAddress}"]'
        heroGameModeTables = self.overwatchUser.response.html.find(css_selector)
        heroDataTables = heroGameModeTables[self.gameMode]
        heroDataCards = heroDataTables.find('.card-stat-block')
        for table in DataTables:
            heroStats[table.name] = GetTableSpecificHeroStats(table, heroDataCards)

        return json.dumps(heroStats)

    def GetTableSpecificHeroStats(self, table, heroDataCards) -> str:
        """
        Gets hero stats for a specific table.

        Parameters:
            table (DataTables): Enum for the table desired.
            heroDataCards (obj): Stat block that holds all cards for the particular hero.
        """
        tableStats = {}
        tableName = tables[table]
        for card in heroDataCards:
            if card.text.startswith(tableName):
                return card.text.split("\n")[1:]
