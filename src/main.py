# coding: utf-8

import sys
sys.path.insert(0, 'model')
import logging
from logging.config import fileConfig
from inventparser import InventParser
from dbloader import DbLoader
from base import session
from member import Member
from designer import Designer
from publisher import Publisher
from langdependence import LangDependence
from location import Location
from member_repo import MemberRepo

_author_ = 'ctomas'
_project_ = 'MRInventory'

LOG_CONFIG_FILE = '../resources/logging_config.ini'
#GAMES_FILE = 'mecatol_games.dat'
INVENTORY_FILE = 'Inventario.xlsx'


def main():
    # Configure logging
    logging.config.fileConfig(LOG_CONFIG_FILE)

    # Parse the game inventory file
    parser = InventParser(INVENTORY_FILE)
    parser.read_file()

    # Get the owner member list
    owner_names = parser.get_owner_names()
    print owner_names

    # Get the shelving list
    shelving_numbers = parser.get_shelving_numbers()
    print shelving_numbers

    # Get the game list
    game_names = parser.get_game_names()
    print game_names


    # Load data into database
    #loader = DbLoader()
    member = MemberRepo.get_member('Carlos Tomas')
    print member

    logging.debug('Loading members...')
    num = 0
    for name in owner_names:
        num += 1
        member = Member(str(num), name)
        logging.debug('Insert member [' + member.to_string() + ']')
        MemberRepo.insert_member(member)

    #print headers
    #print inventory.shape
    #print sorted_inventory
    #print owners

    return


    # Load data into database
    loader = DbLoader()

    # Insert new member
    member = Member(10, u'Carlos Tomás')
    #loader.insert_member(member)
    #logging.debug("Inserted member " + member.to_string())

    # Insert new designer
    designer = Designer(u'Michael Kiesling')
    loader.insert_designer(designer)

    # Insert new publisher
    publisher = Publisher(u'2 Tomatoes')
    loader.insert_publisher(publisher)

    # Insert new location
    location = Location(u'A2', 'Black shelving beside the window')
    loader.insert_location(location)

    # Get language dependence
    level = session.query(LangDependence) \
        .filter(LangDependence.level == 1) \
        .first()
    logging.debug("Level 1: " + level.to_string())


if __name__ == '__main__':
    # Run the main method
    main()
