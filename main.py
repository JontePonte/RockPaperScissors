
# Importera funktioner
from functions import test

# Import av alla spelare
from competitors.simple import AllwaysPaper, TotalyRandom, RockBiasRandom, LastChoice
from competitors.LoseSwitch import LoseSwitchRandom, LoseSwitchSmart, LoseSwitchTricky
from competitors.SmartStatistic import SmartStatisticAll, SmartStatisticFive
from competitors.ContinueWin import ContinueWin80
from competitors.Advanced_v1 import Advanced_v1

class GameMaster():
  def __init__(self):

    # Antal rundor i en match
    self.number_of_rounds = 99

    # Skriv ut "rock", "paper" eller "scissors"
    self.print_choices = False

    # Samla in en array med tävlande
    nr = self.number_of_rounds
    self.players = [
      AllwaysPaper(nr),           # 0
      TotalyRandom(nr),           # 1
      RockBiasRandom(nr),         # 2
      LastChoice(nr),             # 3
      LoseSwitchRandom(nr),       # 4
      LoseSwitchSmart(nr),        # 5
      LoseSwitchTricky(nr),       # 6
      SmartStatisticAll(nr),      # 7
      SmartStatisticFive(nr),     # 8
      ContinueWin80(nr),          # 9
      Advanced_v1(nr)             # 10
      ]
    # Övriga variabler
    self.res = 0

### Kör alla spelare mot varandra och visa resultaten ###
  def tournament(self):
    for p1 in range(len(self.players)):
      for p2 in range(len(self.players)):

        # Fokus ligger bara på resultat för player1
        self.players[p1].new_game()
        self.players[p2].reset_rounds()

        for i in range(self.number_of_rounds):
          #resultatvariabel
          self.res = 0

          # Ny runda
          self.players[p1].new_round()
          self.players[p2].new_round()

          if not p1 == p2:
            # Spelarna väljer
            self.players[p1].choose()
            self.players[p2].choose()

            # Spelarna memorerar alla val
            self.players[p1].save_choice(self.players[p1].choice, self.players[p2].choice)
            self.players[p2].save_choice(self.players[p2].choice, self.players[p1].choice)

            # Spela dem mot varandra och spara resultaten
            # Funktionen "test" gör det den långa vägen
            self.res = test(self.players[p1].choice, self.players[p2].choice)

            # Player1 memorerar resultaten
            if self.res == 1:
              self.players[p1].won()
            elif self.res == 2:
              self.players[p1].lost()
            else:
              self.players[p1].drawn()

            if self.print_choices:
              print(self.players[p1].num2rps(), self.players[p2].num2rps())

      # Print av matchresultat
      print(" ")
      print(self.players[p1].name)
      print("Won ",self.players[p1].victories)
      print("Lost",self.players[p1].losses)
      print("Draw",self.players[p1].draws)
      print("W,L,D",sum(self.players[p1].victories),sum(self.players[p1].losses),sum(self.players[p1].draws))

      # Återställ player1 så de andra kan utmana den sen
      self.players[p1].reset()


# Kör GameMaster
game = GameMaster()
game.tournament()
