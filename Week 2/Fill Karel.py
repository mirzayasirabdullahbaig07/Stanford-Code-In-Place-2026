from karel.stanfordkarel import *

def main():
    fill_row()
    go_back_left()
    turn_right()
    while front_is_clear():
        move()
        turn_right()
        fill_row()
        go_back_left()
        turn_right()
    # Now go to top right corner
    go_to_top_right()

def fill_row():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def go_back_left():
    turn_around()
    while front_is_clear():
        move()

def go_to_top_right():
    # Karel is at top-left facing North, turn East and walk to right wall
    turn_right()
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()