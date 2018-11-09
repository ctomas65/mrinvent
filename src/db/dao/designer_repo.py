# coding: utf-8

import logging
from sqlalchemy import exc
from base import session
from designer import Designer


class DesignerRepo(object):
    """
    This class provides CRUD access to game designer data in database.
    """
    @staticmethod
    def get_designer_by_id(designer_id):
        """
        Get the designer data from database having a given id
        :param designer_id: the designer identifier
        :return: the designer data from database
        """
        return session.query(Designer) \
            .filter(Designer.designer_id == designer_id) \
            .first()

    @staticmethod
    def get_designer_by_name(name):
        """
        Get the game designer data from database having a given name
        :param name: the name of the game designer
        :return: the game designer data from database
        """
        return session.query(Designer) \
            .filter(Designer.name == name) \
            .first()

    @staticmethod
    def get_last_designer():
        """
        Get the last game designer registered in database
        :return:
        """
        return session.query(Designer) \
            .order_by(Designer.designer_id.desc()) \
            .first()

    @staticmethod
    def insert_designer(designer):
        """
        Persists game designer data into database
        :param designer: the game designer data
        :return:
        """
        assert designer is not None, 'Designer not specified'
        try:
            session.add(designer)
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert designer: [" + designer.to_string() + "]: " + str(e))

    @staticmethod
    def update_designer(designer):
        """
        Update the game designer data into database
        :param designer: the updated designer data
        :return:
        """
        assert designer is not None, 'Designer not specified'
        try:
            designer_db = session.query(Designer) \
                .filter(Designer.designer_id == designer.designer_id) \
                .one()
            designer_db = designer
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to update game designer: [" + designer.to_string() + "]: " + str(e))

    @staticmethod
    def delete_designer(designer):
        """
        Delete the game designer data from database
        :param designer: the game designer data to be deleted from database
        :return:
        """
        assert designer is not None, 'Designer not specified'
        try:
            session.query(Designer)\
                .filter(Designer.designer_id == designer.loc_id)\
                .delete()
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to delete game designer [" + designer.to_string() + "]: " + str(e))
