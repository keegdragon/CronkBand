       +--------------------------------------------------------+
       |  CCC  RRRR   OOO  N   N K   K BBBB   AAA  NN   N DDDD  |
       | C   C R   R O   O NN  N K  K  B   B A   A N N  N D   D |
       | C     RRRR  O   O N N N KKK   BBBB  AAAAA N  N N D   D |
       | C   C R   R O   O N  NN K  K  B   B A   A N   NN D   D |
       |  CCC  R   R  OOO  N   N K   K BBBB  A   A N    N DDDD  |
       +--------------------------------------------------------+

                              CRONKBAND
                             VERSION 0.1
          OR: HOW I LEARNED TO STOP WORRYING AND LOVE THE BOY

CronkBand is a home-brewed shameless AngBand rip-off by shameless 
rippers-off Alex Lutton and Keegan Patterson. CronkBand is being 
developed with Python 3 and PyGame, although the 1.0 version may 
include other Python packages (no promises).

The goal for Version 0.1 is to have the foundation in place--meaning 
gamelogic.py, gametools.py, and gameview.py work in tandem to produce 
some sort of a game world that a player can interact with. We have not 
achieved this yet, so this README will serve as a sort of living record 
of what is working, how to make it work, and what is broken at any 
given time.

CronkBand is a labor of love in that we both enjoy ascii rogue-likes 
and want to emulate some of the things we love about them by making our 
own. We will not be using any assets or code from any other projects, 
but the spirit of the game and some of the D&D-inspired mechanics will 
undoubtedly be very similar to existing games.

When CronkBand is playable, we hope that you'll enjoy it. Until then, 
wish us luck!

-Alex and Keegan

                              CRONKBAND
                             VERSION 0.2
                        HONEY, I MOVED THE BOY

In our first update to CronkBand, we have skeleton code for gametools 
and gameview: enough, at least, to put together a very simple game loop 
for gamelogic. This game loop creates an Enounter, puts a single 
Character in that encounter, and changes the position of the player 
according to player input on the directional keys. In order to try this 
out, you will need to run 

python [GAME DIRECTORY]/gamelogic.py

from the terminal. Arrow keys control the '@' and ESC closes the window.
This is pretty far from a completed game, but it's a big step from the 
starting point. Next step: put Piles in the Encounter that the player 
character can scoop up Pac-Man style.
