class OverwatchUser:
    """
    Class to denote an overwatch user.
    """

    _url = 'https://playoverwatch.com/en-us/career/pc/'

    def __init__(self, battletag, html_session):
        """
        Parameters:
            battletag (str): User's battletag in the form of '[userName]#[userNumber]'.
            html_session (HTMLSession): The html session object for obtaining the playoverwatch html.
        """
        self.battletag = battletag.replace('#', '-')
        self.response = html_session.get(self._url + 'us/' + self.battletag)
