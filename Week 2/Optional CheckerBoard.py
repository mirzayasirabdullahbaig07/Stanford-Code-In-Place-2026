from karel.stanfordkarel import *
"""


    1. Karel starts at the bottom-left corner, facing East.
    2. We fill every other square in a checkerboard pattern—column by row.
    3. After filling a row, Karel moves to the next row(if it exists).
    4. This process repeats until all accessible rows are filled.
    5. At the end, Karel returns to the original starting position.
    
"""
def main():
    put_beeper()
    complete_east_line()
    return_main()#
def complete_east_line():
    alternate_to_wall()#
    turn_left()
    if front_is_clear():
        start_next_line()
        turn_left()
        complete_west_line()
def complete_west_line():
    alternate_to_wall()
    turn_right()
    if front_is_clear():
        start_next_line()
        turn_right()
        complete_east_line()
def start_next_line():
    if beepers_present():
        move()
    else:
        move()
        put_beeper()
def alternate_to_wall():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            move()
            put_beeper()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def return_main():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    # Move to far-left wall
    while front_is_clear():
        move()
    turn_left()
    turn_left()
    



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()