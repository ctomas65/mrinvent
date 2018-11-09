# coding=utf-8

from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from base import Base, metadata
from game import Game

t_game_has_designer = Table(
    'game_has_designer', metadata,
    Column('game_id', ForeignKey(u'game.game_id'), primary_key=True, nullable=False, index=True),
    Column('designer_id', ForeignKey(u'designer.designer_id'), primary_key=True, nullable=False, index=True)
)


class Designer(Base):
    __tablename__ = 'designer'

    @property
    def designer_id(self):
        return self.designer_id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    designer_id = Column(INTEGER(11), primary_key=True)
    name = Column(String(250), nullable=False)

    games = relationship(u'Game', secondary=u'game_has_designer')

    def __init__(self, name):
        """
        Initialize the game designer
        :param name: the name of the game designer
        """
        self.name = name

    def to_string(self):
        """
        Get the string representation of this game designer
        :return: the string representation of this game designer
        """
        return "{ id: [" + str(self.designer_id) + \
               "], name: [" + self.name.encode('utf-8').decode('utf-8') + "] }"
