from karel.stanfordkarel import *

def main():
    build_column()
    move_to_next_column()
    build_column()
    move_to_next_column()
    build_column()
    move_to_next_column()
    build_column()

def build_column():
    turn_left()         # face North
    put_beeper()        # row 1
    move()
    put_beeper()        # row 2
    move()
    put_beeper()        # row 3
    move()
    put_beeper()        # row 4
    move()
    put_beeper()        # row 5
    # Return to row 1
    turn_around()
    move()
    move()
    move()
    move()
    turn_left()         # face East

def move_to_next_column():
    move()
    move()
    move()
    move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()