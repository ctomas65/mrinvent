# coding: utf-8

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from base import Base


class Publisher(Base):
    __tablename__ = 'publisher'

    @property
    def designer_id(self):
        return self.designer_id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    publisher_id = Column(INTEGER(11), primary_key=True)
    name = Column(String(45), nullable=False)

    def __init__(self, name):
        """
        Initialize the game publisher
        :param name: the name of the game publisher
        """
        self.name = name

    def to_string(self):
        """
        Get the string representation of this game publisher
        :return: the string representation of this game publisher
        """
        return "{ id: [" + str(self.publisher_id) + \
               "], name: [" + self.name.encode('utf-8').decode('utf-8') + "] }"
