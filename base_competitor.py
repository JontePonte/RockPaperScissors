
# Grundklass för tävlande
class Competitor():
    def __init__(self, nr):
        self.number_of_rounds = nr
        self.choice = 0  # 0 = No Choice
        self.mychoices = [0] * nr  # Array med egna val
        self.otherchoices = [0] * nr  # Array med motståndarens val

        self.name = "No name"
        self.victories = []
        self.losses = []
        self.draws = []
        self.game = -1
        self.round = -1

    # Spara alla val
    def save_choice(self, my, other):
        self.mychoices[self.round] = my
        self.otherchoices[self.round] = other

    # Metod för ny match
    def new_game(self):
        self.game += 1
        self.round = -1
        self.victories.append(0)
        self.losses.append(0)
        self.draws.append(0)

    def reset_rounds(self):
        self.round = -1

    # Ny runda i matchen
    def new_round(self):
        self.round = self.round + 1

    def won(self):
        self.victories[self.game] += 1

    def lost(self):
        self.losses[self.game] += 1

    def drawn(self):
        self.draws[self.game] += 1

    def reset(self):
        self.mychoices = [0] * self.number_of_rounds  # Array med egna val
        self.otherchoices = [0] * self.number_of_rounds  # Array med motståndarens val
        self.victories = []
        self.losses = []
        self.draws = []
        self.game = -1
        self.round = -1

    # Metod för att göra om siffra till ord
    def num2rps(self):
        if self.choice == 1:
            rps = "rock"
        elif self.choice == 2:
            rps = "paper"
        elif self.choice == 3:
            rps = "scissors"
        else:
            rps = "none"
        return rps