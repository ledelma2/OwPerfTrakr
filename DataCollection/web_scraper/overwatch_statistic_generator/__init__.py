import json
from .enums import GameModes
from .lookups import heroes

class OverwatchStatisticGenerator:
    blacklisted_tables = ['Average', 'Best']

    """
    This class is for generating overwatch statistics.

    Attributes:
        overwatch_user (OverwatchUser): The user whose performance statistics are desired.
        game_mode (int): The gamemode for the desired stats.
    """

    def __init__(self, overwatch_user, mode = GameModes.QP):
        """
        Constructor for the OverwatchStatisticGenerator.
        Generates stats for quick play by default.

        Parameters:
            overwatch_user (OverwatchUser): The current overwatch user.
            mode (GameModes)(optional): Enum for the game mode desired.
        """
        self.overwatch_user = overwatch_user
        self.game_mode = 0 if mode == GameModes.QP else 1

    def get_hero_statistics(self, hero) -> dict:
        """
        Generates all statistics for a particular hero.

        Parameters:
            hero (Heroes): Enum for the hero desired.
        """
        hero_stats = {}
        hero_data = []
        hero_stats['Hero'] = hero.name
        hero_address = heroes[hero]
        css_selector = f'div[data-category-id="{hero_address}"]'
        hero_game_mode_tables = self.overwatch_user.response.html.find(css_selector)

        if len(hero_game_mode_tables) > self.game_mode:
            hero_data_tables = hero_game_mode_tables[self.game_mode]
            hero_data_cards = hero_data_tables.find('.card-stat-block')
            for card in hero_data_cards:
                try:
                    table_data = card.text.split("\n")
                    if table_data[0] not in self.blacklisted_tables:
                        hero_data.append(self.__parse_table_data(table_data))

                except:
                    continue

        hero_stats['Data'] = hero_data
        return hero_stats

    def __parse_table_data(self, table_data) -> dict:
        """
        Parses the table stat list into a dictionary.

        Parameters:
            table_data (list): List of table stats to be parsed.
        """
        table_stats = {}
        table_stats["TableName"] = table_data[0]
        for i in range(1, len(table_data), 2):
            if(i + 1 < len(table_data)):
                table_stats[table_data[i]] = table_data[i+1]

        return table_stats
