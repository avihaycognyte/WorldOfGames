#for dev branch
def welcome(name):
  """
  This function greets a person by name and welcomes them to the World of Games (WoG).

  Args:
      name: The name of the person to greet.

  Returns:
      A string containing the greeting message.
  """
  return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
  """
  This function presents the available games, prompts the user for a choice,
  and validates the input. It then prompts for difficulty level and validates that as well.

  Returns:
      A tuple containing the chosen game number (1-3) and difficulty level (1-5).
  """

  print("\nPlease choose a game to play:")
  print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
  print("2. Guess Game - guess a number and see if you chose like the computer")
  print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

  while True:
    try:
      game_choice = int(input("Enter your game choice (1-3): "))
      if game_choice not in range(1, 4):
        raise ValueError("Invalid game choice. Please enter a number between 1 and 3.")
      break
    except ValueError as e:
      print(e)

  print("\nPlease choose game difficulty from 1 to 5:")
  while True:
    try:
      difficulty_level = int(input("Enter difficulty level (1-5): "))
      if difficulty_level not in range(1, 6):
        raise ValueError("Invalid difficulty level. Please enter a number between 1 and 5.")
      break
    except ValueError as e:
      print(e)

  return game_choice, difficulty_level


# Example usage
name = input("Enter your name: ")
print(welcome(name))

game_choice, difficulty_level = load_game()

# Here you can add logic based on the chosen game and difficulty

print(f"\nYou chose game {game_choice} with difficulty {difficulty_level}.")

# Replace the following with the actual game logic for each game
if game_choice == 1:
  print("Starting Memory Game...")
  # Implement Memory Game logic here
elif game_choice == 2:
  print("Starting Guess Game...")
  # Implement Guess Game logic here
elif game_choice == 3:
  print("Starting Currency Roulette...")
  # Implement Currency Roulette logic here


