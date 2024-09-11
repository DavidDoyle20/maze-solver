from line import Line
from point import Point
import time

class Cell:
    def __init__(
            self,
            # Point objects representing top left and bottom right points respectively
            window,
            p1,
            p2,
            has_left_wall=True,
            has_right_wall=True,
            has_top_wall=True,
            has_bottom_wall=True):
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.p1 = p1
        self.p2 = p2
        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y
        self._win = window
        self.visited = False

    def draw(self, line_color="black", fill_color="white"):
        if self.visited:
            line_color = "green"
        if self.has_left_wall:
            color = line_color
        else:
            color = "#d9d9d9"
        line = Line(
            Point(self._x1, self._y1) , Point(self._x1, self._y2)
        )
        line.draw(self._win.canvas, color)
        if self.has_right_wall:
            color = line_color
        else:
            color = "#d9d9d9"
        line = Line(
            Point(self._x2, self._y1) , Point(self._x2, self._y2)
        )
        line.draw(self._win.canvas, color)
        if self.has_top_wall:
            color = line_color
        else:
            color = "#d9d9d9"
        line = Line(
            Point(self._x1, self._y1) , Point(self._x2, self._y1)
        )
        line.draw(self._win.canvas, color)
        if self.has_bottom_wall:
            color = line_color
        else:
            color = "#d9d9d9"
        line = Line(
            Point(self._x1, self._y2) , Point(self._x2, self._y2)
        )
        line.draw(self._win.canvas, color)


    # If undo is false line should be red, gray otherwise    
    def draw_move(self, to_cell, undo=False):
        cell1_center = Point(
            (self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2
        )
        to_cell_center = Point(
            (to_cell.p1.x + to_cell.p2.x) / 2, (to_cell.p1.y + to_cell.p2.y) / 2
        )
        if undo:
            color = "gray"
        else:
            color = "red"
        line = Line(cell1_center, to_cell_center)
        line.draw(self._win.canvas, color)
