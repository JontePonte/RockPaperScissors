from Base_competitor import Competitor
import random


# Välj det som vinner som alternativet som
# är vanligast hos motspelarens alla drag
class SmartStatisticAll(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "SmartSatistic (all)"

    def choose(self):
        if self.round == 0:
            self.choice = random.randint(1, 3)
        else:
            o = self.otherchoices[0:self.round]  # list the other players choice
            oc = o[0]  # variable for most others most common
            counter = 0

            # Find the others most common choice
            for i in o:
                curr_frequency = o.count(i)
                if curr_frequency > counter:
                    counter = curr_frequency
                    oc = i

            # Choose what would win
            if oc == 1:
                self.choice = 2
            elif oc == 2:
                self.choice = 3
            else:
                self.choice = 1


# Välj det som vinner som alternativet som
# är vanligast hos motståndaren de 5 senaste rundorna
class SmartStatisticFive(Competitor):
    def __init__(self, nr):
        Competitor.__init__(self, nr)
        self.name = "SmartStatistic (last 5)"

    def choose(self):
        if self.round <= 4:
            self.choice = random.randint(1, 3)
        else:
            other = self.otherchoices[0:self.round]
            o = other[-5:]  # list the other players 5 last choices
            oc = o[0]  # variable for most others most common
            counter = 0

            # Find the others most common choice
            for i in o:
                curr_frequency = o.count(i)
                if curr_frequency > counter:
                    counter = curr_frequency
                    oc = i

            # Choose what would win
            if oc == 1:
                self.choice = 2
            elif oc == 2:
                self.choice = 3
            else:
                self.choice = 1