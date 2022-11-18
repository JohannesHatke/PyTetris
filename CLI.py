import time
import getch 
from Game import GameState

# file responsible for launching tetris and displaying it on commandline
parsekey = {"a": "LEFT",
        "d": "RIGHT",
        "s": "DOWN"}
def gameLoop(runningG):
    running = True
    starttime = time.time()
    fps = 60
    onceEvery = 1 / fps
    while running:
        char = getch.getch()
        #print(char)
        #print(chr(27) + "[2J")

        print(runningG)
        
        #if char == None:
        time.sleep(onceEvery -((time.time() - starttime) % onceEvery))
        if char in parsekey.keys():
            pass



def main():

    runningG = GameState()
    gameLoop(runningG)



    
    
if __name__ == "__main__":
    main()
