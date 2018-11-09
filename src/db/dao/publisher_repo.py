# coding: utf-8

import logging
from sqlalchemy import exc
from base import session
from publisher import Publisher


class PublisherRepo(object):
    """
    This class provides CRUD access to game publisher data in database.
    """
    @staticmethod
    def get_publisher_by_id(publisher_id):
        """
        Get the game publisher data from database having a given id
        :param publisher_id: the publisher identifier
        :return: the publisher data from database
        """
        return session.query(Publisher) \
            .filter(Publisher.publisher_id == publisher_id) \
            .first()

    @staticmethod
    def get_publisher_by_name(name):
        """
        Get the game publisher data from database having a given number
        :param name: the game publisher name
        :return: the game publisher data from database
        """
        return session.query(Publisher) \
            .filter(Publisher.name == name) \
            .first()

    @staticmethod
    def get_last_publisher():
        """
        Get the last game publisher registered in database
        :return: the last game publisher
        """
        return session.query(Publisher) \
            .order_by(Publisher.publisher_id.desc()) \
            .first()

    @staticmethod
    def insert_publisher(publisher):
        """
        Persists game publisher data into database
        :param publisher: the game publisher data
        :return:
        """
        assert publisher is not None, 'Publisher not specified'
        try:
            session.add(publisher)
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert publisher: [" + publisher.to_string() + "]: " + str(e))

    @staticmethod
    def update_publisher(publisher):
        """
        Update the game publisher data into database
        :param publisher: the updated game publisher data
        :return:
        """
        assert publisher is not None, 'Publisher not specified'
        try:
            publisher_db = session.query(Publisher) \
                .filter(Publisher.publisher_id == publisher.member_id) \
                .one()
            publisher_db = publisher
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to update game publisher: [" + publisher.to_string() + "]: " + str(e))

    @staticmethod
    def delete_publisher(publisher):
        """
        Delete the game publisher data from database
        :param publisher: the game publisher to be deleted from database
        :return:
        """
        assert publisher is not None, 'Publisher not specified'
        try:
            session.query(Publisher)\
                .filter(Publisher.publisher_id == publisher.publisher_id)\
                .delete()
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to delete game publisher [" + publisher.to_string() + "]: " + str(e))
