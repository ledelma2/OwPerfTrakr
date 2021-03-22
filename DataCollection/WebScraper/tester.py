from requests_html import HTMLSession
from overwatch_user import OverwatchUser
from overwatch_statistic_generator import OverwatchStatisticGenerator
from overwatch_statistic_generator.enums import DataTables, Heroes

def main():
    session = HTMLSession()
    overwatchUser = OverwatchUser(battletag = "Serb#11472", htmlSession = session)
    statsGenerator = OverwatchStatisticGenerator(overwatchUser)
    print(statsGenerator.GetHeroStatistics(Heroes.Reinhardt, DataTables.Combat))

if __name__ == '__main__':
    main()
