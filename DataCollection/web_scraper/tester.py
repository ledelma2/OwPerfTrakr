from requests_html import HTMLSession
from overwatch_user import OverwatchUser
from overwatch_statistic_generator import OverwatchStatisticGenerator
from overwatch_statistic_generator.enums import DataTables, Heroes

def main():
    session = HTMLSession()
    overwatchUser = OverwatchUser(battletag = "Surb#11378", htmlSession = session)
    statsGenerator = OverwatchStatisticGenerator(overwatchUser)
    print(statsGenerator.get_hero_statistics(Heroes.Reinhardt))

if __name__ == '__main__':
    main()
