# coding: utf-8

import logging
from sqlalchemy import exc
from base import session
from member import Member


class MemberRepo(object):
    """
    This class provides CRUD access to member data in database.
    """
    @staticmethod
    def get_member_by_id(member_id):
        """
        Get the member data from database having a given id
        :param member_id: the member identifier
        :return: the member data from database
        """
        return session.query(Member) \
            .filter(Member.member_id == member_id) \
            .first()

    @staticmethod
    def get_member_by_number(number):
        """
        Get the member data from database having a given number
        :param number: the member number
        :return: the member data from database
        """
        return session.query(Member) \
            .filter(Member.number == number) \
            .first()

    @staticmethod
    def get_member_by_name(name):
        """
        Get the member data from database having to a given name
        :param name: the member name
        :return: the member data from database
        """
        return session.query(Member) \
            .filter(Member.name == name) \
            .first()

    @staticmethod
    def get_last_member():
        """
        Get the last member registered in database
        :return: the last member
        """
        return session.query(Member) \
            .order_by(Member.member_id.desc()) \
            .first()

    @staticmethod
    def insert_member(member):
        """
        Persists member data into database
        :param member: the member data
        :return:
        """
        assert member is not None, 'Member not specified'
        try:
            session.add(member)
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert member: [" + member.to_string() + "]: " + str(e))

    @staticmethod
    def update_member(member):
        """
        Update the member data into database
        :param member: the updated member data
        :return:
        """
        assert member is not None, 'Member not specified'
        try:
            member_db = session.query(Member) \
                .filter(Member.member_id == member.member_id) \
                .one()
            member_db = member
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to update member: [" + member.to_string() + "]: " + str(e))

    @staticmethod
    def delete_member(member):
        """
        Delete the member data from database
        :param member:
        :return:
        """
        assert member is not None, 'Member not specified'
        try:
            session.query(Member)\
                .filter(Member.member_id == member.member_id)\
                .delete()
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to delete member [" + member.to_string() + "]: " + str(e))
