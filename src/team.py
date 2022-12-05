from typing import List

from src.player import Player


class Team:

    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.teamPlayers: List[Player] = []

    def add_player(self, name,age,height,weight):
        new_player = Player(name,age,height,weight)
        self.teamPlayers.append(new_player)

    def getName(self):
        return self.name










