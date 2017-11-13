from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you
    def __eq__(self, other):
        """
        Return whether MNPuzzle self is equivalent to other.

        @type self: MNPuzzle
        @type other: MNPuzzle | Any
        @rtype: bool
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> m1 = MNPuzzle(start_grid, target_grid)
        >>> m2 = MNPuzzle(start_grid, target_grid)
        >>> m1.__eq__(m2)
        True
        >>> start_grid1 = (("*", "2", "5"), ("1", "4", "5"))
        >>> m3 = MNPuzzle(start_grid1, target_grid)
        >>> m1.__eq__(m3)
        False
        """
        return (type(self) == type(other) and self.from_grid == other.from_grid and self.to_grid == other.to_grid and self.n == other.n and self.n == other.n)

    def __str__(self):
        """
        Return a human-readable string representation of MNPuzzle self.
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> m1 = MNPuzzle(start_grid, target_grid)
        >>> print(m1)
        *23
        145
        """
        result = ''
        for x in self.from_grid:
            for y in x:
                result +=y
            result += '\n'
        return result[:-1]

    # TODO
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"
    def extensions(self):
        """
        Return list of extensions of MNPuzzle self.

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]


        >>> m1 = MNPuzzle((("*", "2", "3"), ("1", "4", "5")), (("1", "2", "3"), ("4", "5", "*")))
        >>> L1 = m1.extensions()
        >>> start_grid1 = (("2", "*", "3"), ("1", "4", "5"))
        >>> start_grid2 = (("1", "2", "3"), ("*", "4", "5"))
        >>> L2 = [MNPuzzle(start_grid1, (("1", "2", "3"), ("4", "5", "*"))), MNPuzzle(start_grid2, (("1", "2", "3"), ("4", "5", "*")))]
        >>> len(L1) == len(L2)
        True
        """
        new_row = ()
        result = []
        new_grid = ()
        other_row = ()
        for row in self.from_grid:
            r = self.from_grid.index(row)
            if '*' in row:
                i = row.index('*')
                #check right
                if i+1 in range(len(row)) and row[i+1] != '*':
                    new_row = row[:i] + (row[i+1],) + (row[i],) + row[i+2:]
                    new_grid = self.from_grid[:r] + (new_row,) + self.from_grid[r+1:]
                    result.append(MNPuzzle(new_grid, self.to_grid))
                #check left
                if i-1 in range(len(row)) and row[i-1] != '*':
                    new_row = row[:i-1] + (row[i],) + (row[i-1],) + row[i+1:]
                    new_grid = self.from_grid[:r] + (new_row,) + self.from_grid[r+1:]
                    result.append(MNPuzzle(new_grid, self.to_grid))
                #check up
                if r-1 in range(len(self.from_grid)) and self.from_grid[r-1][i]:
                    new_row = row[:i] + (self.from_grid[r-1][i],) + row[i+1:]
                    other_row = self.from_grid[r-1][:i] + ('*',) + self.from_grid[r-1][i+1:]
                    new_grid = self.from_grid[:r-1] + (other_row,) + (new_row,) + self.from_grid[r+1:]
                    result.append(MNPuzzle(new_grid, self.to_grid))
                #check down
                if r+1 in range(len(self.from_grid)) and self.from_grid[r+1][i]:
                    new_row = row[:i] + (self.from_grid[r+1][i],) + row[i+1:]
                    other_row = self.from_grid[r+1][:i] + ('*',) + self.from_grid[r+1][i+1:]
                    new_grid = self.from_grid[:r] + (new_row,) + (other_row,) + self.from_grid[r+2:]
                    result.append(MNPuzzle(new_grid, self.to_grid))

        return result


    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid
    def is_solved(self):
        """
        Return whether MNPuzzle self is solved.

        @type self: MNPuzzle
        @rtype: bool

        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> m1 = MNPuzzle(start_grid, target_grid)
        >>> m1.is_solved()
        False
        >>> start_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> m2 = MNPuzzle(start_grid1, target_grid)
        >>> m2.is_solved()
        True
        """
        return (self.from_grid == self.to_grid)



#helper function



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))

