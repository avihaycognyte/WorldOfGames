import random
import time

class MemoryGame:
  """
  This class represents a Memory Game instance.

  Properties:
      difficulty: The difficulty level of the game (integer between 1 and 10).

  Methods:
      generate_sequence(self): Generates a list of random numbers based on difficulty.
      get_list_from_user(self): Prompts the user for a list of numbers and validates them.
      is_list_equal(self, list1, list2): Compares two lists for equality.
      play(self): Starts the memory game loop and returns True if the user wins, False if they lose.
  """

  def __init__(self, difficulty):
    """
    Initializes a MemoryGame instance with the specified difficulty.

    Args:
        difficulty: The difficulty level of the game (integer between 1 and 10).
    """
    if not 1 <= difficulty <= 10:
      raise ValueError("Difficulty level must be between 1 and 10.")
    self.difficulty = difficulty

  def generate_sequence(self):
    """
    Generates a list of random numbers between 1 and 101 based on the difficulty.

    Returns:
        A list of random numbers.
    """
    return random.sample(range(1, 102), self.difficulty)

  def get_list_from_user(self):
    """
    Prompts the user for a list of numbers based on the difficulty and validates them.

    Returns:
        A list of integers entered by the user.
    """
    user_list = []
    for i in range(self.difficulty):
      while True:
        try:
          number = int(input(f"Enter number {i+1}: "))
          if not 1 <= number <= 101:
            raise ValueError("Number must be between 1 and 101.")
          user_list.append(number)
          break
        except ValueError as e:
          print(e)
    return user_list

  def is_list_equal(self, list1, list2):
    """
    Compares two lists for equality.

    Args:
        list1: The first list to compare.
        list2: The second list to compare.

    Returns:
        True if the lists are equal, False otherwise.
    """
    return len(list1) == len(list2) and all(a == b for a, b in zip(list1, list2))

  def play(self):
    """
    Starts the memory game loop.

    Returns:
        True if the user wins, False if they lose.
    """
    print("Get ready to memorize some numbers!")
    sequence = self.generate_sequence()
    print("Here are the numbers:")

    # Display the sequence with adjusted delay based on difficulty
    for number in sequence:
      print(number, end=" ")
      time.sleep(0.7 / self.difficulty)
    print("\nRemember the numbers! Press Enter to continue.")
    input()  # Wait for user to press Enter before continuing

    user_sequence = self.get_list_from_user()

    if self.is_list_equal(sequence, user_sequence):
      print("Congratulations! You remembered all the numbers correctly!")
      return True
    else:
      print("Sorry, you didn't remember all the numbers correctly.")
      print(f"The sequence was: {', '.join(map(str, sequence))}")
      return False
