#write a program to create objects of both the Batsman amd Bowler classes and call the play() method for each object.object.

#Define the base class Player.
class Player:
  def play(self):
    print("The player is playing cricket.")

#Define a derived class Batsman:
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

#create the instances of Batsman and Bowler classes:
player=Player()
batsman=Batsman()
bowler=Bowler()

#call the method play() for each object:
batsman.play()
bowler.play()