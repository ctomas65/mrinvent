# coding: utf-8

import sys
sys.path.insert(0, 'model')
import logging
from sqlalchemy import exc
from base import session
from member import Member


class MemberRepo(Base):
    @staticmethod
    def get_member(name):
        """
        Get the member data from database correponding to a given name
        :param name: the member name
        :return: the member data from database
        """
        return session.query(Member) \
            .filter(Member.name == name) \
            .first()

    @staticmethod
    def insert_member(member):
        """
        Persists member data into database
        :param member: the member data
        :return:
        """
        try:
            if MemberRepo.get_member(member.name) is None:
                session .add(member)
                # Commit session
                session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert member: " + str(e))

    @staticmethod
    def update_member(member):
        """
        Update the member data into database
        :param member: the updated member data
        :return:
        """
        try:
            if MemberRepo.get_member(member.name) is None:
                session.query(Member) \
                    .filter(Member.member_id == member.member_id) \
                    .update(member)
                # Commit session
                session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to update member: " + str(e))
