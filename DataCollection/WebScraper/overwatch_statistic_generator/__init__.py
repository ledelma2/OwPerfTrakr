from .enums import GameModes
from .lookups import dataTables, heroes

"""
Class for generating overwatch statistics.
"""
class OverwatchStatisticGenerator:
    """
    Parameters
    -----------
    overwatchUser : `OverwatchUser`
        OverwatchUser object for the current overwatch user.
    mode : `GameModes`
        GameModes enum for the game mode desired.
    """
    def __init__(self, overwatchUser, mode = GameModes.QP):
        self.overwatchUser = overwatchUser
        self.gameMode = 0 if mode == GameModes.QP else 1

    """
    Parameters
    -----------
    hero : `Heroes`
        Heroes enum for the hero desired.
    table : `DataTables`
        DataTables enum for the table desired.
    """
    def GetHeroStatistics(self, hero, table):
        tableName = dataTables[table]
        heroAddress = heroes[hero]
        css_selector = f'div[data-category-id="{heroAddress}"]'
        heroGameModeTables = self.overwatchUser.response.html.find(css_selector)
        heroDataTables = heroGameModeTables[self.gameMode]
        hereDataCards = heroDataTables.find('.card-stat-block')
        for card in hereDataCards:
            if card.text.startswith(tableName):
                return card.text.split("\n")[1:]
