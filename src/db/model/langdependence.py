# coding: utf-8

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from base import Base


class LangDependence(Base):
    __tablename__ = 'lang_dependence'

    @property
    def lang_id(self):
        return self.lang_id

    @property
    def level(self):
        return self.level

    @level.setter
    def level(self, value):
        self.level = value

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, value):
        self.description = value

    lang_id = Column(INTEGER(11), primary_key=True)
    level = Column(INTEGER(11), nullable=False, unique=True)
    description = Column(String(250), nullable=False)

    def __init__(self, level, description):
        """
        Initialize the language dependency of the game
        :param level: the language dependency level
        :param description: the language dependency description
        """
        self.level = level
        self.description = description

    def to_string(self):
        """
        Get the string representation of this language dependence
        :return: the string representation of this language dependence
        """
        return "{ id: [" + str(self.lang_id) + \
               "], level: [" + str(self.level) + \
               "], description: [" + self.description.encode('utf-8').decode('utf-8') + "] }"
