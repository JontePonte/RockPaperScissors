from base_competitor import Competitor
from functions import test
import random


# Kör på med samma om den vinner, byter annars
class LoseSwitchRandom(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "SwitchRandom when Losing"

    def choose(self):
        # Random första rundan
        if self.round == 0:
            self.choice = random.randint(1, 3)
        else:
            r = self.round
            x = test(self.mychoices[r - 1], self.otherchoices[r - 1])
            # Behåll samma val ifall den vann
            if x == 1:
                self.choice = self.mychoices[r - 1]
            # Byt ifall den blir lika eller den förlorar
            else:
                c = random.randint(1, 3)
                while c == self.mychoices[r - 1]:
                    c = random.randint(1, 3)
                self.choice = c


# Kör på med samma om den vinner,
# byter annars till det som hade vunnit förra rundan
class LoseSwitchSmart(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "SwitchSmart when Losing"

    def choose(self):
        # Random första rundan
        if self.round == 0:
            self.choice = random.randint(1, 3)
        else:
            r = self.round
            x = test(self.mychoices[r - 1], self.otherchoices[r - 1])
            # Behåll samma val ifall den vann
            if x == 1:
                self.choice = self.mychoices[r - 1]
            # Byt ifall den blir lika eller den förlorar
            # Välj det som skulle vinna förra matchen
            else:
                o = self.otherchoices[r - 1]
                if o == 1:
                    self.choice = 2
                elif o == 2:
                    self.choice = 3
                else:
                    self.choice = 1


# Kör på med samma om den vinner,
# byter annars till det som hade gett "draw"
class LoseSwitchTricky(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "SwitchTricky when Losing"

    def choose(self):
        # Random första rundan
        if self.round == 0:
            self.choice = random.randint(1, 3)
        else:
            r = self.round
            x = test(self.mychoices[r - 1], self.otherchoices[r - 1])
            # Behåll samma val ifall den vann
            if x == 1:
                self.choice = self.mychoices[r - 1]
            # Byt ifall den blir lika eller den förlorar
            # Välj det som skulle vinna förra matchen
            else:
                o = self.otherchoices[r - 1]
                if o == 1:
                    self.choice = 1
                elif o == 2:
                    self.choice = 2
                else:
                    self.choice = 3
