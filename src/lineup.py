from typing import List

class LineUp:

    def __init__(self,team):
        self.team = team
        self.player_lineup = list()

    def add_player(self, player):
        self.player_lineup.append(player)



    def player_str(self):
        s = ""
        for p in self.player_lineup:
            s = s + p.name + ","

        return s




