from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    p1 = Point(50, 50)
    p2 = Point(100, 100)
    p3 = Point(101, 50)
    p4 = Point(151, 100)
    line = Line(p1, p2)
    win = Window(1000, 1000)
    cell = Cell(win, p1, p2, True, True, True, True)
    cell2 = Cell(win, p3, p4)

    #cell.draw()
    #cell2.draw()

    #cell.draw_move(cell2, True)

    maze = Maze(2, 2, 32, 32, 25, 25, win)
    maze.solve()

    #win.draw_line(line, "red")

    win.wait_for_close()

main()