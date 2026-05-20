from karel.stanfordkarel import *

def main():
    go_to_piece()
    place_piece()
    return_home()

def go_to_piece():
    # Karel at row 1, col 1 facing East
    # Beeper at row 1, col 3
    move()              # col 2
    move()              # col 3
    pick_beeper()

def place_piece():
    # At row 1, col 3 facing East
    # Target: row 3, col 4
    turn_left()       
    move()              
        
    turn_right()     
    move() 
    turn_left()        
    move()    
    put_beeper()

def return_home():
    # At row 3, col 4 facing East
    # Return to row 1, col 1 facing East
    turn_around()       # face West
    move()              # col 3
    move()              # col 2
    turn_right()     
    move()              
    move()  
    move()
    turn_around()          
        

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()