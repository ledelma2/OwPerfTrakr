from requests_html import HTMLSession
from WebScraper.overwatch_user import OverwatchUser
from WebScraper.overwatch_statistic_generator import OverwatchStatisticGenerator
from WebScraper.overwatch_statistic_generator.enums import DataTables, Heroes

def main():
    session = HTMLSession()
    overwatchUser = OverwatchUser(battletag = "Serb#11472", htmlSession = session)
    statsGenerator = OverwatchStatisticGenerator(overwatchUser)

    for hero in Heroes:
        print(hero.name)
        try:
            print(statsGenerator.GetHeroStatistics(hero, DataTables.Combat))
        except Exception as e:
            print('Exception occured')

if __name__ == '__main__':
    main()
