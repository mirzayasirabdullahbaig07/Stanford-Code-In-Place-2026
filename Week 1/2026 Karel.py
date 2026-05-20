from karel.stanfordkarel import *

def main():
    # Place 20 beepers at first position
    for i in range(20):
        put_beeper()
    
    # Move one step east
    move()
    
    # Place 26 beepers at second position
    for i in range(26):
        put_beeper()
    
    # Move one more step east
    move()

if __name__ == '__main__':
    main()