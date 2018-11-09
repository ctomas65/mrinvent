# coding: utf-8

import logging
import datetime
from base import engine
from member import Member
from location import Location
from member_repo import MemberRepo
from location_repo import LocationRepo


class DbLoader(object):
    # Initializer / Instance Attributes
    def __init__(self):
        """
        Initialize the board game catalogue database loader

        Attributes:
        """
        logging.debug("Tables in database: [" + ', '.join(engine.table_names()) + "]")

    @staticmethod
    def load_members(names):
        """
        Load the game owners as members in database.
        :param names: the list of the game owner names
        :return:
        """
        for name in names:
            # Ignore empty names
            if not name.strip():
                continue
            member = MemberRepo.get_member_by_name(name)
            if member is None:
                # Get the number of the last registered member
                last_num = 0
                last_member = MemberRepo.get_last_member()
                if last_member is not None:
                    last_num = last_member.number
                num = str(int(last_num) + 1)
                now = datetime.datetime.today().strftime('%Y-%m-%d')
                member = Member(num, name, now)
                # Insert new member
                logging.debug('Insert member ' + member.to_string())
                MemberRepo.insert_member(member)
            else:
                logging.debug('Update member ' + member.to_string())
                MemberRepo.update_member(member)

    @staticmethod
    def load_locations(shelving_numbers):
        """
        Load the game shelving as location in database
        :param shelving_numbers: the list of shelves
        :return:
        """
        for shelving_num in shelving_numbers:
            shelving_num = str(shelving_num).strip()
            if not shelving_num.strip():
                continue
            location = LocationRepo.get_location_by_shelving(shelving_num)
            if location is None:
                # Insert a new location
                location = Location(shelving_num)
                logging.debug('Insert location ' + location.to_string())
                LocationRepo.insert_location(location)
            else:
                logging.debug('Update location ' + location.to_string())
                LocationRepo.update_location(location)

    @staticmethod
    def load_games(game_names):
        for name in game_names:
