
from src.tournament import Team

class Player:

    def __init__(self,name,age,height,weight):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight
        self._player_team = Team

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._name

    @property
    def height(self):
        return self._name


    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_weight(self):
        return self._weight

    def get_height(self):
        return self._height

    def get_player_team(self):
        return self._player_team

