from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint

PSEUDOCODE

START STATE: Karel is at (1,1) facing EAST
ASSUMPTIONS: There are infinite beepers in the beeper bag
WORLD      : N X N where N>=1
GOAL STATE: Karel is at (1,N/2)

STEPS:
1. Place Beepers along the first row
2. Move Karel back to (1,1)
3. As long as beepers are present, remove the beepers one each from the
   beginning and end till the beeper at mid-point is remaining.
"""

def main():

    #Place beepers along the entire stretch of first row
    place_beepers()

    #Move Karel back to (1,1)
    backtrack()

    #As long as there are beepers, keep removing one from each end of the row
    while beepers_present():
        remove_beepers()

    #Now Karel is at (1, N/2 + 1)
    #Therefore, move Karel to (1,N/2); put a beeper and reorient facing EAST
    turn_and_move()
    put_beeper()
    turn_around()

    #Reorient Karel to Face
    if facing_west():
        turn_around()

def backtrack():

    # Moves Karel back to (1,1)
    # Pre-condition: Karel is at (1,N) facing EAST
    # Post-condition: Karel is at (1,1) facing EAST

    turn_around()
    while front_is_clear():
        move()
    turn_around()

def place_beepers():

    #Places beepers along the row
    #Pre-condition: Karel is at (1,1) facing EAST
    #               There are no beepers placed.
    #Post-condition: Karel is at (1,N). 
    #                Beepers are placed along the entire row where Karel is present.
    
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

    
def remove_beepers():

    #Removes the beeper one each from the end and beginning, in that order
    #Pre-condition: Karel is at (1,1) Facing EAST with row full of beepers.
    #Post-condition: Karel is at (1, N/2 + 1) Facing EAST with no beepers.

    #Keep moving Karel till last beeper (works both L->R and R-.L)
    while beepers_present() and front_is_clear():
        move()

    #Karel picks beeper and moves to previous cell
    if beepers_present():
        pick_beeper()
        turn_and_move()

    #Karel moves to previous cell; Picks beeper, and moves one more 
    #previous cell
    else:
        turn_and_move()
        pick_beeper()
        move()

def turn_and_move():

    # Karel rotates 180 degrees from current position and moves to previous cell
    turn_around()
    move()
    
def turn_around():

    #Rotates Karel by 180 degrees from its current position
    for _ in range(2):
        turn_left()

if __name__ == '__main__':
    main()