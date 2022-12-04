

class Referee:

    def __init__(self,name,country):
        self._name = name
        self._country = country

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country

    def get_name(self):
        return self.name

    def get_country(self):
        return self.country
