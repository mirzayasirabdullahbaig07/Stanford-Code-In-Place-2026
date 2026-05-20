from karel.stanfordkarel import *

def main():
    draw_left_side()
    draw_right_side()
    draw_middle()

def draw_left_side():
    # Draw left diagonal going up 4 steps
    turn_left()             # face North
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def draw_right_side():
    # From top, go right and down 4 steps
    turn_right()            # face East
    move()
    move()
    turn_right()            # face South
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def draw_middle():
    # Go back up 2 and draw crossbar
    turn_left()             # face East... 
    turn_left()             # face North
    move()
    move()
    turn_left()             # face West
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()