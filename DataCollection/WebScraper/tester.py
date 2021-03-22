from requests_html import HTMLSession
from overwatch_user import OverwatchUser
from overwatch_statistic_generator import OverwatchStatisticGenerator

def main():
    session = HTMLSession()
    overwatchUser = OverwatchUser(battletag = "Serb#11472", htmlSession = session)

if __name__ == '__main__':
    main()
