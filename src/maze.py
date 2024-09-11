from cell import Cell
from point import Point
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed: random.seed(seed)
        print("Starting Construction of Maze")
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        start_tuple = (random.randrange(len(self._cells)-1), random.randrange(len(self._cells[0])-1))
  
        print(start_tuple)

        self._break_walls_r(start_tuple[0], start_tuple[1])
        
        self._reset_cells_visited()
        self._draw_cell()


    def _create_cells(self):
        for c in range(self.num_cols):
            new_col = []
            for r in range(self.num_rows):
                top_left = Point(
                    self.x1+(self.cell_size_x*r),
                    self.y1+(self.cell_size_y*c)
                    )
                bottom_right = Point(
                    top_left.x+self.cell_size_x,
                    top_left.y+self.cell_size_y
                )
                new_col.append(Cell(self.win, top_left, bottom_right))
            self._cells.append(new_col)
        self._draw_cell()


    def _draw_cell(self):
        for x in self._cells:
            for cell in x:
                cell.draw()
                self._animate()

        
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        if len(self._cells) == 0:
            raise Exception("No Cells!")
        elif len(self._cells[0]) == 0:
            raise Exception("Missing entrance")
        elif len(self._cells[len(self._cells)-1]) == 0:
            raise Exception("Missing exit")
        else:
            entrance = self._cells[0][0]
            m_exit = self._cells[-1][-1]
            entrance.has_left_wall = False
            m_exit.has_right_wall = False
            m_exit.draw()
            entrance.draw()

    def _break_walls_r(self, i, j):
        
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check the cells directly adjacent to the current cell and keep track of them
            if self._is_valid_pos(i, j-1):
                if self._cells[i][j-1].visited == False:
                    to_visit.append((i, j-1))
            if self._is_valid_pos(i-1, j):
                if self._cells[i-1][j].visited == False:
                    to_visit.append((i-1, j))
            if self._is_valid_pos(i, j+1):
                if self._cells[i][j+1].visited == False:
                    to_visit.append((i, j+1))
            if self._is_valid_pos(i+1, j):
                if self._cells[i+1][j].visited == False:
                    to_visit.append((i+1, j))
            if len(to_visit) == 0:
                self._draw_cell()
                return
            else:
                # (i,j)
                next_cell = random.choice(to_visit)

                self._break_shared_wall(i,j,next_cell[0], next_cell[1])
                self._break_walls_r(next_cell[0], next_cell[1])


    def _reset_cells_visited(self):
        print("STARTING RESET")
        for x in self._cells:
            for cell in x:
                cell.visited = False

    def _is_valid_pos(self, i, j):
        height = len(self._cells)-1
        width = len(self._cells[0])-1
        if (i < 0 or i > len(self._cells)-1 or j < 0 or j > len(self._cells[0])-1):
            #print("Invalid: ",i, j, "Size:", height, width)
            return False
        return True
    
    def _break_shared_wall(self, i, j, i2, j2):
        if i2 < i:
            self._cells[i][j].has_top_wall = False
            self._cells[i2][j2].has_bottom_wall = False
        if j2 < j:
            self._cells[i][j].has_left_wall = False
            self._cells[i2][j2].has_right_wall = False
        if i2 > i:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i2][j2].has_top_wall = False
        if j2 > j:
            self._cells[i][j].has_right_wall = False
            self._cells[i2][j2].has_left_wall = False
        #self._cells[i][j].draw_move(self._cells[i2][j2])

    def _is_end(self, i, j):
        pass
    
    def solve(self):
        self._solve_r(0,0)
    
    # Returns true if the current cell is an end cell OR if it leads to the end cell
    def _solve_r(self, i, j):
        pass

            
