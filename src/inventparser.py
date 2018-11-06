# coding=utf-8

import logging
import urllib
import urllib2
import httplib
import xml.etree.ElementTree
import pandas as pd
import numpy as np
from bgggame import BGGGame


class InventParser(object):
    """
    Parses a game list

    Attributes:
        BGG_XMLAPI_URL: the BGG XML API base URL
        BGG_XMLAPI_SEARCH_URL: the BGG XML API search URL
        BGG_XMLAPI_BOARDGAME_URL: the BGG XML API boardgame URL
        COMMENT: the character of a comment line in the game list
        SEPARATOR: the character of a data separator in the game list
        filename: the name of the file that contains the game list to be parsed
    """
    # Constants
    BGG_XMLAPI_URL = 'https://boardgamegeek.com//xmlapi/'
    BGG_XMLAPI_SEARCH_URL = BGG_XMLAPI_URL + 'search?search='
    BGG_XMLAPI_BOARDGAME_URL = BGG_XMLAPI_URL + 'boardgame/'

    # Class properties
    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = '../resources/' + value

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value

    # Initializer / Instance Attributes
    def __init__(self, filename):
        """
        Initialize the board game list parser
        :param filename: the name of the file that contains the game inventory
        """
        self.filename = '../resources/' + filename
        self.inventory = None

    def read_file(self):
        """
        Read the game list file line by line
        :return:
        """
        # Load the first sheet of the inventory file into a data frame
        logging.info('Read inventory file [' + self.filename + ']')
        try:
            self.inventory = pd.read_excel(self.filename, sheet_name=0, encoding='utf-8')
            if self.inventory is not None:
                self.inventory = self.inventory.replace(np.nan, '', regex=True)
        except Exception as ex:
            logging.error('Failed to read inventory file [' + self.filename + ']: ' + str(ex))

    def get_owner_names(self):
        """
        Get the list of unique owner names as read from the inventory file
        :return: the list of unique owner names
        """
        owner_names = []
        if self.inventory is not None:
            owner_names = self.inventory['PROPIETARIO'].tolist()
            owner_names = sorted(set([name.title() for name in owner_names]))
        return owner_names

    def get_game_names(self):
        """
        Get the list of game names as read from the inventory file
        :return: the list of game names
        """
        game_names = []
        if self.inventory is not None:
            game_list = self.inventory['NOMBRE DEL JUEGO'].tolist()
            for name in game_list:
                if isinstance(name, (int, long, float)):
                    game_names.append(str(name))
                else:
                    name = name.strip('\"').strip('\'')
                    game_names.append(name.encode('utf-8'))
            game_names = sorted(set(game_names))
        return game_names

    def get_shelving_numbers(self):
        """
        Get the list of shelving numbers as read from the inventory file
        :return: the list of shelving numbers
        """
        shelving_numbers = []
        if self.inventory is not None:
            shelving_list = self.inventory['ESTANTERIA'].tolist()
            for number in shelving_list:
                if isinstance(number, (int, long, float)):
                    shelving_numbers.append(str(number))
                else:
                    number = number.strip('\"').strip('\'')
                    shelving_numbers.append(number.encode('utf-8'))
            shelving_numbers = sorted(set(shelving_list))
        return shelving_numbers

    def search_game(self, name):
        """
        Search a board game by a given name
        :param name: the board game name
        :return:
        """
        game = None
        games = []
        # Get the matching object ids by searching the given name
        objectids = self.search_objectids(name)
        for objectid in objectids:
            game = self.get_game_data(objectid)
            if game is not None:
                games.append(game)
        # Sort found games by objectid
        games = sorted(games, key=lambda g: g.objectid, reverse=False)
        if len(games) > 0:
            game = games[0]
        for game in games:
            logging.debug('Game data: ' + game.to_string().encode('utf-8').decode('utf-8'))

    def search_objectids(self, name):
        """
        Search the object ids of related board games matching the given name
        :param name: the name of the board game to search
        :return: the ids of the board games matching the given name
        """
        object_ids = []
        url = self.BGG_XMLAPI_SEARCH_URL + urllib.quote(name)
        logging.info('Search game: ' + url)
        try:
            response = urllib2.urlopen(url)
            xmldata = response.read()
            # Get the ids found by board game name
            root = xml.etree.ElementTree.fromstring(xmldata)
            for boardgame in root.findall('boardgame'):
                objectid = int(boardgame.attrib.get('objectid'))
                if objectid is not None:
                    object_ids.append(objectid)
        except urllib2.HTTPError, ex:
            logging.error('HTTPError = ' + str(ex.code))
        except urllib2.URLError, ex:
            logging.error('URLError = ' + str(ex.reason))
        except httplib.HTTPException, ex:
            logging.error('HTTPException = ' + ex.message)
        except Exception:
            import traceback
            logging.error('Generic exception: ' + traceback.format_exc())

        return object_ids

    def get_game_data(self, objectid):
        """
        Get the board game data
        :param objectid: the BGG id of the game board
        :return:
        """
        game = None
        try:
            # Query the board game data
            url = self.BGG_XMLAPI_BOARDGAME_URL + str(objectid)
            response = urllib2.urlopen(url)
            xmldata = response.read()
            root = xml.etree.ElementTree.fromstring(xmldata)
            boardgame = root.find('boardgame')
            if boardgame is not None:
                # Get the game data
                name = self.get_name(boardgame)
                year = self.get_year(boardgame)
                designers = self.get_designers(boardgame)
                publishers = self.get_publishers(boardgame)
                minplaytime = self.get_minplaytime(boardgame)
                maxplaytime = self.get_maxplaytime(boardgame)
                playtime = (minplaytime, maxplaytime)
                minplayers = self.get_minplayers(boardgame)
                maxplayers = self.get_maxplayers(boardgame)
                players = (minplayers, maxplayers)
                suggested = self.get_suggested(boardgame)
                age = self.get_age(boardgame)
                language = 'N/A'
                image = self.get_image(boardgame)
                description = self.get_description(boardgame)
                # Build the game object
                game = BGGGame(objectid, name, year, designers, publishers,
                               playtime, players, suggested, age, language, image, description)
        except urllib2.HTTPError, ex:
            logging.error('HTTPError = ' + str(ex.code))
        except urllib2.URLError, ex:
            logging.error('URLError = ' + str(ex.reason))
        except httplib.HTTPException, ex:
            logging.error('HTTPException = ' + ex.message)
        except Exception:
            import traceback
            logging.error('Generic exception: ' + traceback.format_exc())
        return game

    def get_name(self, boardgame):
        """
        Get the board game name
        :param boardgame: the boardgame XML node
        :return:
        """
        name = None
        for bgname in boardgame.findall('name'):
            if bgname.attrib.get('primary') == 'true':
                name = bgname.text.encode('utf-8')
        return name

    def get_year(self, boardgame):
        """
        Get the board game publishing year
        :param boardgame: the boardgame XML node
        :return: the board game publishing year
        """
        return boardgame.find('yearpublished').text \
            if boardgame.find('yearpublished') is not None \
            else None

    def get_designers(self, boardgame):
        """
        Get the board game designer list
        :param boardgame: the boardgame XML node
        :return: the board game designer list
        """
        designers = []
        for designer in boardgame.findall('boardgamedesigner'):
            designers.insert(0, designer.text.encode('utf-8'))
        return designers

    def get_publishers(self, boardgame):
        """
        Get the board game publisher list
        :param boardgame: the boardgame XML node
        :return: the board game publisher list
        """
        publishers = []
        for publisher in boardgame.findall('boardgamepublisher'):
            publishers.insert(0, publisher.text.encode('utf-8'))
        return publishers

    def get_minplaytime(self, boardgame):
        """
        Get the board game minimum play time
        :param boardgame: the boardgame XML node
        :return: the board game minimum play time
        """
        return boardgame.find('minplaytime').text \
            if boardgame.find('minplaytime') is not None \
            else None

    def get_maxplaytime(self, boardgame):
        """
        Get the board game maximum play time
        :param boardgame: the boardgame XML node
        :return: the board game maximum play time
        """
        return boardgame.find('maxplaytime').text \
            if boardgame.find('maxplaytime') is not None \
            else None

    def get_minplayers(self, boardgame):
        """
        Get the board game minimum number of players
        :param boardgame: the boardgame XML node
        :return: the minimum number of players
        """
        return boardgame.find('minplayers').text \
            if boardgame.find('minplayers') is not None \
            else None

    def get_maxplayers(self, boardgame):
        """
        Get the board game maximum number of players
        :param boardgame: the boardgame XML node
        :return: the maximum number of players
        """
        return boardgame.find('maxplayers').text \
            if boardgame.find('maxplayers') is not None \
            else None

    def get_suggested(self, boardgame):
        """
        Get the number of suggested players from the BGG poll results
        :param boardgame: the boardgame XML node
        :return:
        """
        suggested = None
        maxvotes = 0
        suggested_poll = self.get_poll(boardgame, 'suggested_numplayers')
        for results in suggested_poll.findall('results'):
            numplayers = results.attrib['numplayers']
            for result in results.findall('result'):
                if result.attrib['value'] == 'Best':
                    numvotes = result.attrib['numvotes']
                    if numvotes > maxvotes:
                        maxvotes = numvotes
                        suggested = numplayers
        return suggested

    def get_age(self, boardgame):
        """
        Get the recommended age to play the board game
        :param boardgame: the boardgame XML node
        :return: the recommended age to play the board game
        """
        return boardgame.find('age').text \
            if boardgame.find('age') is not None \
            else None

    def get_image(self, boardgame):
        """
        Get the image of the board game
        :param boardgame: the boardgame XML node
        :return: the image of the board game
        """
        return boardgame.find('image').text.encode('utf-8') \
            if boardgame.find('image') is not None \
            else None

    def get_description(self, boardgame):
        """
        Get the detailed description of the board game
        :param boardgame: the boardgame XML node
        :return: the detailed description of the board game
        """
        return boardgame.find('description').text.encode('utf-8') \
            if boardgame.find('description') is not None \
            else None

    def get_poll(self, boardgame, poll_name):
        """
        Get the poll XML node matching the given name
        :param boardgame: the boardgame XML node
        :param poll_name: the poll name
        :return:
        """
        poll = None
        polls = boardgame.findall('poll')
        for pollnode in polls:
            if pollnode.attrib.get('name') == poll_name:
                poll = pollnode
                break
        return poll
