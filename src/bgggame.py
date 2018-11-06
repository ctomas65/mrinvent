from utils import xstr


class BGGGame(object):
    """
    This class contains the game board data

    Attributes:
        objectid: the BGG id of the board game
        name: the name of the board game
        year: the publishing year
        designers: the game board designers
        publishers: the game board publishers
        playtime: the average play time
        players: the number of players
        suggested: the suggested number of players
        age: the minimum age of play
        language: the language dependency
        image: the game board image
        description: the game board description
    """
    # Class properties
    @property
    def objectid(self):
        return self._objectid

    @objectid.setter
    def objectid(self, value):
        self._objectid = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def designers(self):
        return self._designers

    @designers.setter
    def designers(self, value):
        self._designers = value

    @property
    def publishers(self):
        return self._publishers

    @publishers.setter
    def publishers(self, value):
        self._publishers = value

    @property
    def playtime(self):
        return self._playtime

    @playtime.setter
    def playtime(self, value):
        self._playtime = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = value

    @property
    def suggested(self):
        return self._suggested

    @suggested.setter
    def suggested(self, value):
        self._suggested = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language= value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    # Initializer / Instance Attributes
    def __init__(self, objectid=0, name="", year=0, designers=[], publishers=[],
                 playtime=(), players=(), suggested=0, age=0, language="", image="", description=""):
        """
        Initialize the game data
        :param objectid: the BGG id of the board game
        :param name: the name of the board game
        :param year: the publishing year
        :param designers: the game board designers
        :param publishers: the game board publishers
        :param playtime: the average play time
        :param players: the number of players
        :param suggested: the suggested number of players
        :param age: the minimum age of play
        :param language: the language dependency
        :param image: the game board image
        :param description: the game board description
        """
        self._objectid = objectid
        self._name = name
        self._year = year
        self._designers = designers
        self._publishers = publishers
        self._playtime = playtime
        self._players = players
        self._suggested = suggested
        self._age = age
        self._language = language
        self._image = image
        self._description = description

    def to_string(self):
        return "{ objectid: [" + xstr(self.objectid) + \
                "], name: [" + xstr(self.name) + \
                "], year: [" + xstr(self.year) + \
                "], designer: [" + ','.join(self.designers) + \
                "], publisher: [" + ','.join(self.publishers) + \
                "], playtime: (" + "-".join(self.playtime) + \
                "), players: (" + "-".join(self.players) + \
                "), suggested: [" + xstr(self.suggested) + \
                "], age: [" + xstr(self.age) + \
                "], language: [" + xstr(self.language) + \
                "], image: [" + xstr(self.image) + \
                "], description: [" + xstr(self.description) + "] " + \
                "}"

