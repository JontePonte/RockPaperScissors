from Base_competitor import Competitor
import random


# Alltid "paper"
class AllwaysPaper(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "AllwaysPaper"

    def choose(self):
        self.choice = 2  # 2 = paper


# Helt random
class TotalyRandom(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "TotalyRandom"

    def choose(self):
        self.choice = random.randint(1, 3)


# Random men gillar sten
# Killar väljer mest sten. Denna gör det 50 % av dragen
class RockBiasRandom(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "Random but RockBias"

    def choose(self):
        x = random.randint(1, 4)
        if x == 4:
            self.choice = 1  # 50 % sten
        else:
            self.choice = x


# Välj motståndarens förra val
class LastChoice(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "Oponents LastChoice"

    def choose(self):
        if self.round == 0:
            self.choice = random.randint(1, 3)
        else:
            self.choice = self.otherchoices[self.round - 1]
