from utils import randbool
from utils import randcell
from utils import randcell2

class Map:
    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x > self.h or y > self.w:
            return False
        return True

    def generate_rivers(self, l):
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range (w)] for j in range(h)]
    
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self):
        c = randcell(self.h, self.w)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    def generate_fires(self):
        cc = randcell(self.h, self.w)
        ccx, ccy = cc[0], cc[1]
        if self.cells[ccx][ccy] == 1:
            self.cells[ccx][ccy] = 3
    
    def update_fires(self):
        for rri in range(self.h):
            for cci in range(self.w):
                if self.cells[rri][cci] == 3:
                    self.cells[rri][cci] = 0
        for i in range(5):
            self.generate_fires()

    def print_map(self):
        print('⬛' * (self.w + 2))
        for row in self.cells:
            print('⬛', end = '')
            for cell in row:
                if cell >= 0 and cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end = '')
            print('⬛')
        print('⬛' * (self.w + 2))
    
    

CELL_TYPES = '🟩🌲🌊🔥🏥🏭'
    

       