import random

class GuessGame:
  """
  This class represents a Guess Game instance.

  Properties:
      difficulty: The difficulty level of the game (integer between 1 and 5).
      secret_number: The randomly generated number to guess (integer between 1 and difficulty).

  Methods:
      generate_number(): Generates a random number based on the difficulty.
      get_guess_from_user(): Prompts the user for a guess and validates it.
      compare_results(guess): Compares the guess with the secret number and returns feedback.
      play(): Starts the game loop and returns True if the user wins, False if they lose.
  """

  def __init__(self, difficulty):
    """
    Initializes a GuessGame instance with the specified difficulty.

    Args:
        difficulty: The difficulty level of the game (integer between 1 and 5).
    """
    self.difficulty = difficulty
    self.secret_number = None

  def generate_number(self):
    """
    Generates a random number between 1 and the difficulty level.
    """
    self.secret_number = random.randint(1, self.difficulty)

  def get_guess_from_user(self):
    """
    Prompts the user for a guess and validates it within the difficulty range.

    Returns:
        The user's guess as an integer.
    """
    while True:
      try:
        guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
        if 1 <= guess <= self.difficulty:
          return guess
        else:
          print("Invalid guess. Please enter a number within the specified range.")
      except ValueError:
        print("Invalid input. Please enter a number.")

  def compare_results(self, guess):
    """
    Compares the guess with the secret number and returns feedback.

    Args:
        guess: The user's guess to compare.

    Returns:
        A string indicating the result (too high, too low, or correct).
    """
    if guess == self.secret_number:
      return "Congratulations! You guessed the number correctly!"
    elif guess < self.secret_number:
      return "Too low, try again!"
    else:
      return "Too high, try again!"

  def play(self):
    """
    Starts the guess game loop.

    Returns:
        True if the user wins, False if they lose.
    """
    self.generate_number()
    print("Guessing game started!")

    while True:
      guess = self.get_guess_from_user()
      result = self.compare_results(guess)
      print(result)

      if guess == self.secret_number:
        return True
      else:
        play_again = input("Do you want to play again (y/n)? ").lower()
        if play_again != "y":
          break

# Example usage is commented out to prevent execution when imported
# difficulty = int(input("Enter difficulty level (1-5): "))
# game = GuessGame(difficulty)
# if game.play():
#   print("You won!")
# else:
#   print("You lost. The secret number was", game.secret_number)
