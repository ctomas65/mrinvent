# coding: utf-8

import sys
sys.path.insert(0, 'model')
import logging
from sqlalchemy import exc
from base import engine
from base import session
from member import Member


class DbLoader(object):
    # Initializer / Instance Attributes
    def __init__(self):
        """
        Initialize the board game catalogue database loader

        Attributes:
            engine: the engine to interact with the database, it manages pools and dialects
            session:

        """
        logging.debug("Tables in database: [" + ', '.join(engine.table_names()) + "]")

    @staticmethod
    def get_member(name):
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
            if DbLoader.get_member(member.name) is None:
                session.add(member)

                # Commit session
                session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert member: " + str(e))

    @staticmethod
    def insert_designer(designer):
        """
        Persists designer data into database
        :param designer: the designer data
        :return:
        """
        try:
            session.add(designer)

            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert designer " + designer.to_string() + ": " + str(e))

    @staticmethod
    def insert_publisher(publisher):
        """
        Persists publisher data into database
        :param publisher: the publisher data
        :return:
        """
        try:
            session.add(publisher)

            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert publisher " + publisher.to_string() + ": " + str(e))

    @staticmethod
    def insert_location(location):
        """
        Persists location data into database
        :param location: the location data
        :return:
        """
        try:
            session.add(location)

            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert location " + location.to_string() + ": " + str(e))
