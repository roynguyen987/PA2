from typing import List

from src.tournament.LineUp import LineUp
from src.tournament.Referee import Referee
from src.tournament.Team import Team


class Match:

    def __init__(self, date_time):
        self._date_time = date_time
        self._scoreTeamA = 0
        self._scoreTeamB = 0
        teamA = Team("", "")
        teamB = Team("", "")
        self.matchRefs = List[Referee] = []
        teamALU = LineUp("")
        teamBLU = LineUp("")

    @property
    def date_time(self):
        return self._date_time

    @property
    def scoreTeamA(self):
        return self._scoreTeamA

    @property
    def scoreTeamB(self):
        return self._scoreTeamB

    def get_date_time(self):
        return self.date_time
    def get_scoreTeamA(self):
        return self.scoreTeamA
    def get_scoreTeamB(self):
        return self.scoreTeamB
    
