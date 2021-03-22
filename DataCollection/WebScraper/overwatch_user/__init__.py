"""
Class to denote an overwatch user.
"""
class OverwatchUser:
    _url = 'https://playoverwatch.com/en-us/career/pc/'

    """
    Parameters
    -----------
    battletag : `str`
        User's battletag in the form of '[userName]#[userNumber]'.
    htmlSession : `HTMLSession`
        The html session object for obtaining the playoverwatch html.
    """
    def __init__(self, battletag, htmlSession):
        self.battletag = battletag.replace('#', '-')
        print('Getting html session response...')
        self.response = htmlSession.get(self._url + 'us/' + self.battletag)
        print('Html session response recieved...')
