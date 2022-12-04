from typing import List
from Tournament import Tournament
from src.tournament import Player
from src.tournament.Country import Country


class Team:

    def __init__(self, name, country):
        self._name = name
        self._country = country
        self.teamPlayers = List[Player] = []