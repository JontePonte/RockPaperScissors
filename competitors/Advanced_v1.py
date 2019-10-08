from Base_competitor import Competitor
import random


# Advance v1
class Advanced_v1(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "Advanced v1"

        # Sannorlihet att välja rock, paper & scissors
        self.rc = 0.333
        self.pc = 0.333
        self.sc = 0.333

        self.change = 0.05  # Variable för sannorlikens ändringshastighet
        self.min_change = 0.01  # Minsta tillåtna ändringshastighet
        self.max_change = 0.1  # Högsta tillåtna ändrignshastighet

    def choose(self):
        if not self.round == 1:  # Updatera sannorliheten om ej runda 1
            self.update_prob()

        # Randomvariabel
        rand = random.random()
        if rand <= self.rc:  # Test av "rock"
            self.choice = 1
        elif rand <= (self.rc + self.pc):  # Test av "paper"
            self.choice = 2
        else:  # Annars "scissors"
            self.choice = 3

    # Updatera sannorlikheterna
    def update_prob(self):
        last = self.round - 1

        if self.mychoices[last] == 1:
            x = self.update_change_rate(self.rc)
            if self.otherchoices[last] == 2:
                self.rc = self.rc - x
                self.pc = self.pc + x
            elif self.otherchoices[last] == 3:
                self.rc = self.rc + x
                self.sc = self.sc - x

        elif self.mychoices[last] == 2:
            x = self.update_change_rate(self.pc)
            if self.otherchoices[last] == 1:
                self.pc = self.pc + x
                self.rc = self.rc - x
            elif self.otherchoices[last] == 3:
                self.pc = self.pc - x
                self.sc = self.sc + x

        elif self.mychoices[last] == 3:
            x = self.update_change_rate(self.sc)
            if self.otherchoices[last] == 1:
                self.sc = self.sc - x
                self.rc = self.rc + x
            elif self.otherchoices[last] == 2:
                self.pc = self.pc - x
                self.sc = self.sc + x

    # Ta fram ny förändringshastighet för sannorlikheten
    def update_change_rate(self, prob):
        x = self.change * prob
        if x < self.min_change:
            x = self.min_change
        elif x > self.max_change:
            x = self.max_change
        return x

    # Advanced v1 behöver en egen new_game för att nollställa chanse-variablerna
    def new_game(self):
        self.game += 1
        self.round = -1
        self.victories.append(0)
        self.losses.append(0)
        self.draws.append(0)
        self.rc = 0.333
        self.pc = 0.333
        self.sc = 0.333