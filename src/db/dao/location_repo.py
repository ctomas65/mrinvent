# coding: utf-8

import logging
from sqlalchemy import exc
from base import session
from location import Location


class LocationRepo(object):
    """
    This class provides CRUD access to location data in database.
    """
    @staticmethod
    def get_location_by_id(loc_id):
        """
        Get the location data from database having a given id
        :param loc_id: the location identifier
        :return: the location data from database
        """
        return session.query(Location) \
            .filter(Location.loc_id == loc_id) \
            .first()

    @staticmethod
    def get_location_by_shelving(shelving):
        """
        Get the location data from database having a given shelving number
        :param shelving: the shelving number
        :return: the location data from database
        """
        return session.query(Location) \
            .filter(Location.shelving == shelving) \
            .first()

    @staticmethod
    def get_last_location():
        """
        Get the last location registered in database
        :return:
        """
        return session.query(Location) \
            .order_by(Location.loc_id.desc()) \
            .first()

    @staticmethod
    def insert_location(location):
        """
        Persists location data into database
        :param location: the location data
        :return:
        """
        assert location is not None, 'Location not specified'
        try:
            session.add(location)
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to insert location: [" + location.to_string() + "]: " + str(e))

    @staticmethod
    def update_location(location):
        """
        Update the location data into database
        :param location: the updated location data
        :return:
        """
        assert location is not None, 'Location not specified'
        try:
            location_db = session.query(Location) \
                .filter(Location.loc_id == location.loc_id) \
                .one()
            location_db = location
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to update location: [" + location.to_string() + "]: " + str(e))

    @staticmethod
    def delete_location(location):
        """
        Delete the location data from database
        :param location: the location data to be deleted from database
        :return:
        """
        assert location is not None, 'Location not specified'
        try:
            session.query(Location)\
                .filter(Location.loc_id == location.loc_id)\
                .delete()
            # Commit session
            session.commit()
        except (exc.SQLAlchemyError, exc.DBAPIError) as e:
            logging.error("Failed to delete location [" + location.to_string() + "]: " + str(e))
