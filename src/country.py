class Country:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        string = 'Country Name: {:s}'.format(self.name)
        return string