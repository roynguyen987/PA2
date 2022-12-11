from typing import List
import datetime
from country import Country
from team import Team
from player import Player
from referee import Referee
from lineup import LineUp
from match import Match



class Tournament:
    name = ""
    start_date = ""

    # Constructor
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.teamPlayers: List[Player] = []
        self.teams: List[Team] = []
        self.players: List[Player] = []
        self.matches: List[Match] = []
        self.line_ups: List[LineUp] = []
        self.referees: List[Referee] = []
        self.countries: List[Country] = []

    # Getters and Setters
    def set_name(self, name):
        self.name = name
    def set_start_date(self, start_date):
        self.start_date = start_date
    def set_end_date(self, end_date):
        self.end_date = end_date

    # Add functions
    def add_country(self, country_name):
        self.countries.append(Country(country_name))

    def add_team(self, team_name, country):
        self.teams.append(Team(team_name, country))

    def add_ref(self, refname, country):
        self.referees.append(Referee(refname, country))

    def add_lineup(self, team):
        self.line_ups.append(LineUp(team))

    def add_player(self, playername, age, height, weight):
        self.players.append(Player(playername, age, height, weight))

    def add_match(self, dt, teamA, teamB):
        self.matches.append(Match(dt, teamA, teamB))

    def add_ref_to_match(self, dt, ref_name):
        for match in self.matches:
            if match.date_time == dt:
                for ref in self.referees:
                    if ref.name.lower() == ref_name:
                        match.add_referee(ref)

    # Other functions
    def set_match_score(self, date_time1, team_a_score, team_b_score):
        for match in self.matches:
            if match.date_time == date_time1:
                match.set_score_team_a(team_a_score)
                match.set_score_team_b(team_b_score)
                match.set_match_score(team_a_score, team_b_score)

    def get_upcoming_matches(self):
        return self.matches

    def get_matches_on(self, match_date):
        matches_on: List[Match] = []
        for match in self.matches:
            m_date = match.date_time
            m_date = m_date.datetime.date()
            if m_date == match_date:
                matches_on.append(match)

        return matches_on

    def get_matches_for(self, team_name):
        matches_for: List[Match] = []
        for match in self.matches:
            team_a = match.get_team_a()
            team_b = match.get_team_b()
            if team_name.lower() == team_a.name or team_name.lower() == team_b.name:
                matches_for.append(match)
        return matches_for

    def get_match_lineUps(self, match_date):
        match_lineups: List[LineUp] = []
        for m in self.matches:
            if m.date_time == match_date:
                for l in self.line_ups:
                    if m.teamA.get_name == l.team.name:
                        match_lineups.append(l)
                    if m.teamB.get_name == l.team.name:
                        match_lineups.append(l)

        return match_lineups

    def add_player_to_lineup(self, player, team):
        if not self.line_ups:
            print("Creating new lineup.")
            lu = LineUp(team)
            lu.add_player(player)
            self.line_ups.append(lu)
            return
        for l in self.line_ups:
            if l.team == team:
                l.add_player(player)
                return
        print("Creating new lineup.")
        l = LineUp(team)
        l.add_player(player)
        self.line_ups.append(l)

    def __str__(self):
        string = 'This is the {:s} tournament.|'.format(self.name)
        return string
