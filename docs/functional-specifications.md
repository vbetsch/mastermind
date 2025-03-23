# Functional specifications

Mastermind is a puzzle game in which a player must guess a secret color combination in a limited number of attempts. In
this virtual version, the computer generates the secret combination and evaluates the player's suggestions.

## Starting and ending

The player can start a new game from the main menu. The game ends when the player correctly guesses the combination
(win) or exhausts all attempts (lose). A message displays the result (win or lose).

## Game rules

* **Secret combination generation**: The computer randomly generates a combination according to the defined parameters.
* **Proposal evaluation**: For each player's proposal, the number of red and white pieces is calculated.
* **Victory condition**: The player wins if he discovers the combination before exhausting his attempts.
* **Defeat condition**: The player loses if he hasn't discovered the combination after using up all his attempts.

## Progress monitoring

For each suggestion, the game displays :

* The number of attempts.
* The proposed combination.
* The number of red units (right colors in the right place).
* The number of white units (right colors in the wrong place).
* A history of previous attempts is displayed to help players refine their proposals.

## Save and restore game

The player can save the current game at any time via the play menu. A saved game can be resumed later from the main
menu.
