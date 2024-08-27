This is a beginner level project.
No hard concepts or oops is used here, just basic python and file handling.

Project Explanation:
    This Python program is a simple gambling game where a player rolls a certain number of dice and bets virtual currency called GGC (Gamble Game Coins). The goal is to match the numbers on all the rolled dice. If the player succeeds, they win a large prize. Here's a breakdown of the code:

### 1. *Introduction and Rules*
   - The game begins by displaying the rules, which are:
     - The player chooses how many dice to roll (between 2 and 6).
     - If all dice show the same number, the player wins a large prize.
     - The more dice rolled, the harder it is to win, but the prize is larger.
     - Players start with 50,000 GGC.
     - The minimum bet is 1000 GGC, and there is no maximum limit.
   - The player decides whether to continue with the game.

### 2. **Username Management (Name function)**
   - The user is prompted to enter their username. If they are new, they can create a new one.
   - If a new username is chosen, the program checks if it already exists. If not, it saves the new username to a file (file.txt) and assigns 50,000 GGC to the new user in another file (Score.txt).

### 3. **Current Score (current_score function)**
   - This function reads the Score.txt file to retrieve the player's current GGC balance based on their username.

### 4. **Rolling Dice (Num_dice function)**
   - The player selects how many dice they want to roll, between 2 and 6.

### 5. **Generating Dice Rolls (luck function)**
   - This function generates a list of random numbers (1 to 6) for each die.

### 6. **Displaying the Dice Roll (Rolling_dice function)**
   - The dice roll is visually represented using ASCII art based on the numbers generated.

### 7. **Checking for Win (result function)**
   - This function checks if all the numbers in the dice roll are the same (indicating a win).

### 8. **Updating the Score (UpdateScore function)**
   - If the player wins, the function calculates the prize based on the formula gamble * (6**(number_of_dice - 1)) and updates the player's score in the Score.txt file.

### 9. **Deducting Gamble Amount (Money_left_after_gambling function)**
   - This function deducts the bet amount from the player's current score, updating the file.

### 10. *Game Execution*
   - The game then proceeds in the following sequence:
     1. The player's current GGC balance is retrieved.
     2. The player decides how much GGC to gamble.
     3. The dice are rolled.
     4. The program checks if the player won.
     5. The player's GGC balance is updated based on the result of the roll.
     6. The final balance is displayed.

### 11. *Exit Option*
   - The player can exit the game at any time by choosing not to continue after seeing the game rules.

### *Flow Summary*
1. *Start*: The player reads the game rules and chooses to continue or exit.
2. *Login*: The player logs in or registers as a new user.
3. *Gambling*: The player selects the number of dice, makes a bet, and rolls the dice.
4. *Result*: The program checks if the player won and updates their balance accordingly.
5. *End*: The updated balance is displayed, and the game can be played again or exited.

This program uses text files (file.txt for usernames and Score.txt for scores) to manage user data and simulate a gambling environment with virtual currency.



There are a lot of way where you can improve this program.You can add your own methods and characters too. Stay tuned and follow my github profile for more unique projects like this.
