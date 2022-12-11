from typing import List
import datetime
from src.referee import Referee
from src.team import Team


class Match:

    # Constructor
    def __init__(self, date_time, teamA, teamB):
        self.date_time = date_time
        self.scoreTeamA = 0
        self.scoreTeamB = 0
        self.teamA = Team("","")
        self.teamB = Team("","")
        self.matchRefs= list()
        self.teamALU = None
        self.teamBLU = None


    # Add functions
    def add_player(self, player, team):
        team.add_player(player.name, player.age, player.height, player.weight)

    def add_referee(self, ref):
        self.matchRefs.append(ref)

    def set_match_score(self, score_team_a, score_team_b):
        self.scoreTeamA = score_team_a
        self.scoreTeamB = score_team_b

    def get_date_time(self) -> datetime:
        return self.date_time

    def set_score_team_a(self, score_team_a):
        self.scoreTeamA = score_team_a

    def set_score_team_b(self, score_team_b):
        self.scoreTeamB = score_team_b

    def __str__(self):
        now = datetime.now()
        string = ""
        if self.date_time > now:
            string = 'Match Date: {:s} || Team 1: {:s} || Team2: {:s} || Team1 Score: {:d} || Team2 Score: {:d}'.format(
                self.date_time, self.teamA.name, self.teamB.name,
                self.scoreTeamA, self.scoreTeamB)
        else:
            string = 'Match Date: {:s} || Team 1: {:s} || Team2: {:s}'.format(
                self.date_time, self.teamA.name, self.teamB.name)
        return string
