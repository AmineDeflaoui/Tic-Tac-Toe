# Tic-Tac-Toe

## Introduction
The application is a game called 'tic-tac-toe' where the user can play against the computer or against a person.
First window is an interface that contains the game name and a button to start the game. After clicking the button, you will see two buttons: the first is played against the computer and the second against a person, after choosing, a place will appear for you to write the name of the player (players). After that, you can start playing and when winning, a page will appear with the name of the winner, or in case of a tie, a message will appear "tie". And to apply all these things, we used the Python 3 language.
Finally we used Tkinter, it is the original free graphics library for the Python language which allows the creation of graphical interfaces for the code.

## Application
### Classes :
Window class 1 (mother class) is the one that controls the shape of windows, contains the title, length, width, color and its location on the screen, a create function to create a frame contains the name Tic -Tac-Toe and a 'play' button and a 'play-clicked' function that allows us to switch from window 1 to window 2 (New interface to choose the game mode player against player or player against computer), it there are also other classes used in the script for the other windows of the game, we will detail them in the next part (inheritance).

### inheritance :
We have used 5 classes (child classes) which are inherited from the parent class (window 1).
        The first class (window 2) is to create a window with the same parameters as the mother window, and it contains a function (create) which creates two buttons and also contains two functions (player_player and player_computer) to activate the request held by each button, if the user has chosen player versus player a window appears one enter the names of the players and start the game, and the choice and player versus computer another window used for the name of the only player and a button to play.

The second and third classes (window 3 and window 4) have a window creation function which contains 'Label' and 'Entry' and we have functions which are somewhat similar to one for player against player which retains the names of players and we create a new class (window), the same for the other class which contains the 'player_computer' function which has the same role as the preceding function except that it will just retain the name of the player and start the game immediately.
The fourth class (window 5) inherited from the window1 class, new parameters added to the previous inherited parameters and this class contains:
- The (create) function for the window interface.
- The button_clicked function: is activated when the user clicks on a button, and its role is to check if there is an X or an O on this button (exception, next part) and to choose a letter (X by default for the first player) and put it in the button (configure the button) if it wasn't there before.
- The case_verification function: You check the victory conditions if one of the two players to win a function wins activates otherwise you have pressed 9 buttons so all the kicks are activated but there is no winner, so there declare equality.
- The function wins: creates another window to display the name of the winner or the message "tie" in case of a tie.
- The ok_clicked function: deletes the open windows and creates a window to start playing again.
Finally the class (window 6) contains the same functions as those of window 5 with little change in the button_clicked function since now the user is going to play against the computer so the change that was made is the program choosed randomly the empty button and configure them with the letter O since we always give the letter X for user who starts first in all the time.

### Exceptions : 
The exception is used twice in our program, the first when the user name is not entered, the user left the field empty, it displayed a message "enter the name yourself". The second in the classes (window5 and window6) is the case when the same button is clicked to place a letter and it already has a letter in it so the program will show you a message from (Warning or Error) button already used .

### Libraries :
We used “from tkinter. Messagebox import” to use showerror which display the Name or Button error.
We used "import random" to use the random function for the program choose a variable (buttons) randomly when the player against the computer (see class window6, function button_clicked ()).
