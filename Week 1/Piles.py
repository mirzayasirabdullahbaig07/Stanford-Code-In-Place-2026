from karel.stanfordkarel import *

def main():
    # Move through all 6 columns, picking up beepers wherever they exist
    for i in range(6):
        move()
        while beepers_present():
            pick_beeper()

if __name__ == '__main__':
    main()