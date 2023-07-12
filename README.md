# Higher Lower Game

The Higher Lower Game is a simple Python project that allows you to play a game where you guess the follower count of various celebrities or social media profiles. The project consists of three files: `main.py`, `art.py`, and `game_data.py`. This readme file provides an overview of the project and instructions on how to use it.

## Files

- `main.py`: This is the main file of the project that contains the game logic and user interface. It imports the `game_data` module to access the data and uses the `art` module for ASCII art.
- `art.py`: This file includes ASCII art used for visual enhancements in the game.
- `game_data.py`: This module contains the data used by the game. It includes a list named `data` that stores information about various celebrities, social media profiles, and organizations.

## Data

The `data` list in the `game_data.py` module contains information about different profiles. Each profile is represented as a dictionary with the following properties:

- `name`: The name of the celebrity, social media profile, or organization.
- `follower_count`: The number of followers or subscribers for the profile.
- `description`: A brief description of the profile or organization.
- `country`: The country associated with the profile or organization.

The data provided in this project is for demonstration purposes and may not reflect real-time follower counts. It is generated or sourced for illustrative purposes only. Feel free to modify or extend the data list with additional profiles to make the game more challenging or interesting.

## Usage

To play the Higher Lower Celebrity Follower Game, follow these steps:

1. Ensure you have Python installed on your system.
2. Download or clone the project files to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the game:
   ```
   python main.py
   ```
5. Follow the instructions displayed in the terminal to play the game. You will be presented with two profiles and need to guess which one has a higher or lower follower count.
6. After each guess, the game will inform you if your guess is correct and display the current score.
7. Continue guessing until lose!

Have fun playing the Higher Lower Game and test your knowledge of celebrity follower counts!

## Credits

The following game was inspired by [http://www.higherlowergame.com/]
