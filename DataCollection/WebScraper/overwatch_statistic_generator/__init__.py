from overwatch_user import OverwatchUser
from .enums import GameModes

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
    hero : `str`
        User's battletag in the form of '[userName]#[userNumber]'.
    """
    def GetHeroStatistics(self, hero):
        print('Hello')
