# coding: utf-8

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from base import Base


class Location(Base):
    __tablename__ = 'location'

    @property
    def loc_id(self):
        return self.loc_id

    @property
    def shelving(self):
        return self.shelving

    @shelving.setter
    def shelving(self, value):
        self.shelving = value

    @property
    def comments(self):
        return self.comments

    @comments.setter
    def comments(self, value):
        self.comments = value

    loc_id = Column(INTEGER(11), primary_key=True)
    shelving = Column(INTEGER(11))
    comments = Column(String(250))

    def __init__(self, shelving, comments=''):
        """
        Initialize the game location
        :param shelving: the shelving number the game is located in
        :param comments: relevant comments related to the location
        """
        self.shelving = shelving
        self.comments = comments

    def to_string(self):
        """
        Get the string representation of the game location
        :return: the string representation of this game designer
        """
        return "{ id: [" + str(self.loc_id) + \
               "], shelving: [" + self.shelving.encode('utf-8').decode('utf-8') + \
               "], comments: [" + self.comments.encode('utf-8').decode('utf-8') + "] }"
