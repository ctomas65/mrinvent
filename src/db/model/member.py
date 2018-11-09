# coding: utf-8

import datetime
from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.mysql import INTEGER
from base import Base


class Member(Base):
    __tablename__ = 'member'

    @property
    def member_id(self):
        return self.member_id

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, value):
        self.number = value

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def subscription_date(self):
        return self.subscription_date

    @subscription_date.setter
    def subscription_date(self, value):
        self.subscription_date = value

    member_id = Column(INTEGER(11), primary_key=True)
    number = Column(String(45), nullable=False)
    name = Column(String(250), nullable=False)
    subscription_date = Column(Date, default=datetime.datetime.today().strftime('%Y-%m-%d'))

    def __init__(self, number, name, subscription_date=None):
        """
        Constructor.
        Initialize any member instance when created.
        :param number: the member number
        :param name: the member name and surname
        :param subscription_date: the subscription date
        """
        self.number = number
        self.name = name
        self.subscription_date = subscription_date

    def __eq__(self, other):
        """
        Equal to comparison method
        :param other: the other instance to be compared to this
        :return:  true if the member numbers are equal, false otherwise
        """
        return self.number == other.number

    def to_string(self):
        """
        Get the string representation of this member
        :return: the string representation of this member
        """
        return "{ id: [" + str(self.member_id) + \
               "], number: [" + self.number.encode('utf-8').decode('utf-8') + \
               "], name: [" + self.name + \
               "], subscription_date: [" + str(self.subscription_date) + "] }"
