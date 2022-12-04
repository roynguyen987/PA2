from typing import List
from src.tournament import Match
from src.tournament import Player
from src.tournament import LineUp
from src.tournament import Referee
from src.tournament import Country
from src.tournament import Team



class Tournament:

    name = ""
    start_date = ""


    def __init__(self, name,start_date, end_date):
        self._name = name
        self._start_date = start_date
        self._end_date = end_date
        self.teams = List[Team] = []
        self.players = List[Player] = []
        self.matches = List[Match] = []
        self.line_ups = List[LineUp] = []
        self.referees = List[Referee] = []
        self.countries = List[Country] = []


    @property
    def name(self):
        return self._name

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    def get_name(self):
        return self.name
    def get_start_date(self):
        return self.start_date
    def get_end_date(self):
        return self._end_date


    def get_teams(self):
        return self.teams

    def get_players(self):
        return self.players

    def get_matches(self):
        return self.matches

    def get_line_ups(self):
        return self.line_ups

    def get_referees(self):
        return self.referees

    def get_countries(self):
        return self.countries












