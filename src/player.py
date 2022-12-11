

class Player:

    # Construcotr
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.player_team = None

    # Getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def get_player_team(self):
        return self.player_team

    def __str__(self):
        string = 'Name: {:s} || Age: {:s} || Height: {:s} || Weight: {:s}'.format(self.name, self.age, self.height,
                                                                     self.weight)
        return string
