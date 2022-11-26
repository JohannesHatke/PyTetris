
# positons list always starts top left moves to right and then down
# up left corner is always (0,0)
class Piece():
    def __init__(self, positions=[(0,0),(0,1),(-1,0),(-1,1)]):
        self.positions = positions

    def moveUp(self, y):
        newpos = []
        for pos in self.positions:
            (oldx,oldy) = pos
            newpos.append((oldx,oldy+y))
    
    def move(self, direction) -> list:
        #return new positions after move or rotation in that direction
        directions = { 
                "DOWN": (0,-1),
                "LEFT": (-1,0),
                "RIGHT":(1,0)
                }
        if not direction in directions.keys():
            raise Exception("Piece.move(): invalid direction")
        output = []
        (x,y) = directions[direction]
        print(f"\n\nmoving {direction}")
        for pos in self.positions:
            (oldx,oldy) = pos
            output.append((oldx + x, oldy+y))

        return output
        
    def updatePositions(self,positions:list[tuple]):
        #update new position
        if len(positions) != 4: raise Exception("Piece.updatePosition(): new positions too long")
        self.positions = positions


class Square(Piece):
    def __init__(self):
        super().__init__(positions=[(0,0),(0,1),(-1,0),(-1,1)])
    def rotateLeft():
        pass
    def rotateRight():
        pass

class GameState():
    def __init__(self, leny = 20, lenx = 10):
        self.leny = leny
        self.lenx = lenx
        self.field = [[None for j in range(lenx)] for i in range(leny+4)] #m = moving/ s=settled/ None = nothing
        firstPiece = Square()
        firstPiece.moveUp(10)
        firstPiece.positions = [(2,0),(2,1),(1,0),(1,1)]
        self.currentPiece = firstPiece
        for pos in firstPiece.positions:
            (x,y) = pos
            self.field[y][x] = "m"

    def __repr__(self):
        c = u'\u2588'
        s = 2*c
        output = ""
        for line in self.field:
            output += "\t|"
            for entry in line:
                if entry == "m": 
                    output += s
                elif entry == "s":
                    output += s
                else: output += "  "
            output += "|\n"

        output += str(self.currentPiece.positions)
        return output

    def validMove(self, positions) -> bool:
        for pos in positions:
            (x,y) = pos
            if x < 0 or x >= self.lenx:
                return False
            if y < 0 or y >= self.leny:
                return False
            if not (self.field[x][y] == None or self.field[x][y] == "m"):
                return False
        return True

    def moveCurrentPiece(self, direction):
        newPos = self.currentPiece.move(direction)
        if(self.validMove(newPos)):
            self.currentPiece.updatePositions(newPos)
            for pos in newPos:
                (x,y) = pos
                self.field[y][x] = "m"
    def fall(self):
        newPos = self.currentPiece.move("DOWN")
        if(validMove(newPos)):
            currentPiece.updatePositions(newPos)
            for pos in positions:
                (x,y) = pos
                self.field[y][x] = "m"
            return True
        else: return False
    


            

