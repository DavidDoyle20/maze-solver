import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    win = Window(1000,1000)
    '''def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, self.win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )'''
    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        flag = True
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, self.win, 2342)
        for x in m1._cells:
            for cell in x:
                if cell.visited:
                    flag = False
        print(m1._cells[0][1].has_left_wall, m1._cells[0][1].has_top_wall, m1._cells[0][1].has_right_wall, m1._cells[0][1].has_bottom_wall, m1._cells[0][1].visited)
        self.assertTrue(flag, "Not all cells were reset")

if __name__ == "__main__":
    unittest.main()