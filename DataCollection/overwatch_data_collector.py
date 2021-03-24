import json
import sys
from requests_html import HTMLSession
from web_scraper.overwatch_user import OverwatchUser
from web_scraper.overwatch_statistic_generator import OverwatchStatisticGenerator
from web_scraper.overwatch_statistic_generator.enums import GameModes, Heroes

class OverwatchDataCollector:
    """
    Class to collect the overwatch data.
    """
    def __init__(self, user_battletag, game_mode):
        """
        Parameters:
            user_battletag (str): The user's battletag in format [name]#[id].
            game_mode (str): The game mode desired for the statistics
                "QP" = "Quick Play"
                "Comp" = "Competitive"
        """
        session = HTMLSession()
        overwatch_user = OverwatchUser(battletag = user_battletag, html_session = session)
        if game_mode.lower() == 'qp':
            self.stats_generator = OverwatchStatisticGenerator(overwatch_user, GameModes.QP)
        elif game_mode.lower() == 'comp':
            self.stats_generator = OverwatchStatisticGenerator(overwatch_user, GameModes.COMP)
        else:
            exception_mssg = f'Command "{game_mode}" is invalid'
            raise BaseException(exception_mssg)

    def get_all_hero_stats(self) -> str:
        """
        Gets a json array string for all heroes associated to the profile.
        """
        hero_stat_list = []
        for hero in Heroes:
            hero_stat_list.append(self.stats_generator.get_hero_statistics(hero))

        return json.dumps(hero_stat_list)

data_collector = OverwatchDataCollector('Surb#11378', 'qp')
print(data_collector.get_all_hero_stats())
