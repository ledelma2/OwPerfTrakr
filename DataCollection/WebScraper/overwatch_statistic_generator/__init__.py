import json
from .enums import DataTables, GameModes
from .lookups import data_tables, heroes

class OverwatchStatisticGenerator:
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
        hero_address = heroes[hero]
        css_selector = f'div[data-category-id="{hero_address}"]'
        hero_game_mode_tables = self.overwatch_user.response.html.find(css_selector)
        hero_data_tables = hero_game_mode_tables[self.game_mode]
        hero_data_cards = hero_data_tables.find('.card-stat-block')
        for table in DataTables:
            hero_stats[table.name] = self.__get_table_specific_stats(table, hero_data_cards)

        return hero_stats

    def __get_table_specific_stats(self, table, hero_data_cards) -> dict:
        """
        Gets specific table stats.

        Parameters:
            table (DataTables): Enum for the table desired.
            hero_data_cards (list): Stat block that holds all cards for the particular hero.
        """
        table_stats = {}
        table_data = []
        table_name = data_tables[table]
        for card in hero_data_cards:
            if card.text.startswith(table_name):
                table_data = card.text.split("\n")[1:]
                break

        return self.__parse_table_data(table_data)

    def __parse_table_data(self, table_data) -> dict:
        """
        Parses the table stat list into a dictionary.

        Parameters:
            table_data (list): List of table stats to be parsed.
        """
        table_stats = {}
        for i in range(0, len(table_data), 2):
            table_stats[table_data[i]] = table_data[i+1]

        return table_stats
