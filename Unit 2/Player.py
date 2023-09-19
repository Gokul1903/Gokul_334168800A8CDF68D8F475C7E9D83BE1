class Player:
    """Cricket players"""
    def play(self):
        print("The player is playing cricket.".title())
class Batsman(Player):
    def play(self):
        print("The batsman is batting.".title())
class Bowler(Player):
    def play(self):
        print("The Bowler is bowlinng.".title())

obj1=Batsman()
obj2=Bowler()

obj1.play()
obj2.play()
