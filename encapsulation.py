
class ScoreBoard:
  def __init__(self, score):
    self.__score = score

  def get_score(self):
    return self.__score

# Create an object
s1 = ScoreBoard(100)

# Print the score
print(s1.get_score())
