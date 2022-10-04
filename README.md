TORPEDO!

TORPEDO is a Python terminal game. which runs in the Code Institute mock terminal on Heroku

/* game descript and live link
External user’s goal:
The application user wants to play a logic game

Site owner's goal:
The Battleships game is played on grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
The application provides a working battleships game for a single user to play against the computer .e.g.

Potential features to include:
The ability for the user to set the grid size
Warn the user if their guess is off-grid

image of terminal display
How to play section
Features section 
  - existing features ( random board generation, user input, maintain scores, input validation and error check, data maintainance
  - future features
Data Model : board class - one for each competitor, stores board size, ship no, ship position, guesses agains the board, players name
              methods in class to help play : print method to print out current board, an add_ship method to add  ships and an add_guess method to add guess and                     return result
## Constraints
The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

Testing
Manual by
  - passing PEP8 linter
  - testing on local terminal and CI Heroku terminal
  - invalid imput statements???
 Bugs
 -solved
 -remaining
 Validator testing results (PEP8)
 ##The website pep8online.com is currently down. We generally recommend that students use this website to validate their Python code before submission.
As a workaround, you can add a PEP8 validator to your Gitpod Workspace directly by following these steps:
Run the command pip3 install pycodestyle  Note that this extension may already be installed, in which case this command will do nothing.
In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results (image 1).
Select pycodestyle from the list (image 2).
PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.
 
Deployment:
This project was deployed using Code Institute's mock terminal for Heroku
  -STeps for deployment:
      -Fork or clone this repository
      -Create a new Heroku app
      - Set the Buildbacks to heruko/python and heroku/nodejs in that order
      - Link the Heroku app to the repository
      Click on Deploy
      
##Credits
- Code Insititure for the deployment terminal
- Hasbro for the experience of playing Battleship, the tactile game this is based on.
- https://coderspacket.com/battleship-game-in-python for further instructions to help construct the game
- 
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.
