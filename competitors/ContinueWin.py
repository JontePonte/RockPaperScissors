from base_competitor import Competitor
from functions import test
import random


# 80 % chans att fortsätta med samma drag om
# den vinner, annars random
class ContinueWin80(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "Continue if Winning (80%)"

    def choose(self):
        if self.round == 0:
            self.choice = random.randint(1, 3)
        else:
            t = test(self.mychoices[self.round - 1], self.otherchoices[self.round - 1])
            if t == 1:
                if random.random() < 0.8:
                    self.choice = self.mychoices[self.round - 1]
                else:
                    self.choice = random.randint(1, 3)
            else:
                self.choice = random.randint(1, 3)
