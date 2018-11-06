# coding: utf-8

from sqlalchemy import Column, String, Enum, Text, Table, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from base import Base
from langdependence import LangDependence
from location import Location
from member import Member
from publisher import Publisher


class Game(Base):
    __tablename__ = 'game'

    @property
    def game_id(self):
        return self.game_id

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        self.title = value

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, value):
        self.type = value

    @property
    def category(self):
        return self.category

    @category.setter
    def category(self, value):
        self.category = value

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, value):
        self.year = value

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        self.age = value

    @property
    def max_players(self):
        return self.max_players

    @max_players.setter
    def max_players(self, value):
        self.max_players = value

    @property
    def min_players(self):
        return self.min_players

    @min_players.setter
    def min_players(self, value):
        self.min_players = value

    @property
    def min_playtime(self):
        return self.min_playtime

    @min_playtime.setter
    def min_playtime(self, value):
        self.min_playtime = value

    @property
    def max_playtime(self):
        return self.max_playtime

    @max_playtime.setter
    def max_playtime(self, value):
        self.max_playtime = value

    @property
    def suggested(self):
        return self.suggested

    @suggested.setter
    def suggested(self, value):
        self.suggested = value

    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, value):
        self.image = value

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, value):
        self.description = value

    @property
    def publisher_id(self):
        return self.publisher_id

    @publisher_id.setter
    def publisher_id(self, value):
        self.publisher_id = value

    @property
    def lang_id(self):
        return self.lang_id

    @lang_id.setter
    def lang_id(self, value):
        self.lang_id = value

    @property
    def owner_member_id(self):
        return self.owner_member_id

    @owner_member_id.setter
    def owner_member_id(self, value):
        self.owner_member_id = value

    @property
    def hired_member_id(self):
        return self.hired_member_id

    @hired_member_id.setter
    def hired_member_id(self, value):
        self.hired_member_id = value

    @property
    def location_id(self):
        return self.location_id

    @location_id.setter
    def location_id(self, value):
        self.location_id = value

    game_id = Column(INTEGER(11), primary_key=True)
    title = Column(String(250), nullable=False)
    type = Column(Enum(u'BOARD', u'MINIATURES', u'RPG'), nullable=False)
    category = Column(String(45))
    year = Column(INTEGER(11))
    age = Column(INTEGER(11))
    min_playtime = Column(INTEGER(11))
    max_playtime = Column(INTEGER(11))
    min_players = Column(INTEGER(11))
    max_players = Column(INTEGER(11))
    suggested = Column(INTEGER(11))
    image = Column(String(250))
    description = Column(Text)
    publisher_id = Column(ForeignKey(u'publisher.publisher_id'), nullable=False, index=True)
    lang_id = Column(ForeignKey(u'lang_dependence.lang_id'), nullable=False, index=True)
    owner_member_id = Column(ForeignKey(u'member.member_id'), index=True)
    hired_member_id = Column(ForeignKey(u'member.member_id'), index=True)
    location_id = Column(ForeignKey(u'location.loc_id'), index=True)

    hired_member = relationship(u'Member', primaryjoin='Game.hired_member_id == Member.member_id')
    lang = relationship(u'LangDependence')
    location = relationship(u'Location')
    owner_member = relationship(u'Member', primaryjoin='Game.owner_member_id == Member.member_id')
    publisher = relationship(u'Publisher')

    def __init__(self, title, type, category, year, age, min_playtime, max_playtime,
                 min_players, max_players, suggested, publisher_id, lang_id,
                 owner_member_id, hired_member_id, location_id):
        """
        Initialize the board game data
        :param title: the title of the board game
        """
        self.title = title
        self.type = type
        self.category = category
        self.year = year
        self.age = age
        self.publisher_id = publisher_id
        self.min_playtime = min_playtime
        self.max_playtime = max_playtime
        self.min_players = min_players
        self.max_players = max_players
        self.suggested = suggested
        self.publisher_id = publisher_id
        self.lang_id = lang_id
        self.owner_member_id = owner_member_id
        self.hired_member_id = hired_member_id
        self.location_id = location_id
