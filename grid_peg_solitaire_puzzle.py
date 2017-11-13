from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # TODO
    # implement __eq__, __str__ methods
    # __repr__ is up to you
    def __eq__(self, other):
        """
        Return whether GridPegSolitairePuzzle self is equivalent to other.

        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle | Any
        @rtype: bool
        >>> marker = [['#', '.', '#', '#']]
        >>> marker.append(['#', '#', '#', '#'])
        >>> marker.append(['#', '*', '#', '#'])
        >>> marker.append(['#', '#', '#', '#'])
        >>> d1 = GridPegSolitairePuzzle(marker, {'#', '.', '*'})
        >>> marker = [['#', '.', '#', '#']]
        >>> marker.append(['#', '#', '#', '#'])
        >>> marker.append(['#', '*', '#', '#'])
        >>> marker.append(['#', '#', '#', '#'])
        >>> d2 = GridPegSolitairePuzzle(marker, {'#', '.', '*'})
        >>> d1.__eq__(d2)
        True
        >>> marker = [['#', '*', '#', '#']]
        >>> marker.append(['#', '.', '#', '#'])
        >>> marker.append(['#', '.', '#', '#'])
        >>> marker.append(['#', '#', '#', '#'])
        >>> d3 = GridPegSolitairePuzzle(marker, {'#', '.', '*'})
        >>> d1.__eq__(d3)
        False
        """
        return(type(self) == type(other) and
               self._marker == other._marker and
               self._marker_set == other._marker_set)

    def __str__(self):
        """
        Return a human-readable string representation of
        GridPegSolitairePuzzle self.
        >>> grid = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", ".", "*", "*"], ["*", "*", "*", "*", "*"]]
        >>> d = GridPegSolitairePuzzle(grid, {'#', '.', '*'})
        >>> print(d)
        *****
        *****
        *****
        **.**
        *****
        """
        s = ''
        for lst in self._marker:
            for i in lst:
                s += i
            s += '\n'
        return s[:-1]

    # TODO
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration

    def extensions(self):
        """
        Return list of extensions of GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]

        >>> grid = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '.']]
        >>> d = GridPegSolitairePuzzle(grid, {'#', '.', '*'})
        >>> L1 = d.extensions()
        >>> len(L1) == 2
        True

        >>> grid = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", ".", "*", "*"], ["*", "*", "*", "*", "*"]]
        >>> d = GridPegSolitairePuzzle(grid, {'#', '.', '*'})
        >>> L1 = d.extensions()
        >>> grid1 = [["*", "*", "*", "*", "*"], ["*", "*", ".", "*", "*"], ["*", "*", ".", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]

        >>> grid2 = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", ".", "."], ["*", "*", "*", "*", "*"]]

        >>> grid3 = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], [".", ".", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
        >>> L2 = [GridPegSolitairePuzzle(grid1, {'#', '.', '*'}), GridPegSolitairePuzzle(grid2, {'#', '.', '*'}), GridPegSolitairePuzzle(grid3, {'#', '.', '*'})]
        >>> len(L1) == len(L2)
        True
        """
        n = len(self._marker[0])
        all_lst = gather_list(self._marker)
        result = []
        i = 0
        grid = []
        while i in range(len(all_lst)):
            if all_lst[i] == '.':
                r = i // n
                #check left
                if i-2 in range(r*n, (r*n)+n) and all_lst[i-1] == '*' and all_lst[i-2] == "*":
                    L = all_lst[:]
                    L[i] = '*'
                    L[i-1] = '.'
                    L[i-2] = '.'
                    grid = separate_list(L, n)
                    result.append(GridPegSolitairePuzzle(grid, {'#', '.', '*'}))
                #check right
                if i+2 in range(r*n, (r*n)+n) and all_lst[i+1] == '*' and all_lst[i+2] == "*":
                    R = all_lst[:]
                    R[i] = '*'
                    R[i+1] = '.'
                    R[i+2] = '.'
                    grid = separate_list(R, n)
                    result.append(GridPegSolitairePuzzle(grid, {'#', '.', '*'}))
                #check down
                if i+(n*2) in range(len(all_lst)) and all_lst[i+n] == '*' and all_lst[i+(n*2)] == '*':
                    D = all_lst[:]
                    D[i] = '*'
                    D[i+n] = '.'
                    D[i+(n*2)] = '.'
                    grid = separate_list(D, n)
                    result.append(GridPegSolitairePuzzle(grid, {'#', '.', '*'}))
                #check up
                if i-(n*2) in range(len(all_lst)) and all_lst[i-n] == '*' and all_lst[i-(n*2)] == '*':
                    U = all_lst[:]
                    U[i] = '*'
                    U[i-n] = '.'
                    U[i-(n*2)] = '.'
                    grid = separate_list(U, n)
                    result.append(GridPegSolitairePuzzle(grid, {'#', '.', '*'}))
            i += 1
        return result



    # TODO
    # override is_solved
    # A configuration is solved when there is exactly one "*" left
    def is_solved(self):
        """
        Return whether GridPegSolitairePuzzle self is solved.
        When there is exactly one '*' left.

        @type self: GridPegSolitairePuzzle
        @rtype: bool

        >>> grid = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '.']]
        >>> d = GridPegSolitairePuzzle(grid, {'#', '.', '*'})
        >>> d.is_solved()
        False

        >>> grid = [['.', '.', '.'], ['.', '*', '.'], ['.', '.', '.']]
        >>> d = GridPegSolitairePuzzle(grid, {'#', '.', '*'})
        >>> d.is_solved()
        True
        """
        copy = gather_list(self._marker)
        count = 0
        for x in copy:
            if x == '*':
                count += 1
            if count > 1:
                return False
        return (count == 1)

    def fail_fast(self):
        """
        If there is only one extension and it just go back to the prev puzzle.
        """
        puzzle = self
        if not self.extensions():
            return True
        elif len(self.extensions()) == 1 and len(self.extensions()[0].extensions()) == 1 and puzzle in self.extensions()[0].extensions():
            return True
        else:
            return False






#helper function
def gather_list(obj):
    if not isinstance(obj, list):
        return [obj]
    else:
        result = []
        for x in obj:
            result += gather_list(x)
        return result

def separate_list(d, n):
    """
    Percondition: number of item in lst is the multiple of n.
    @type lst: list
    @type n: int
    @rtype: list of list

    >>> d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    >>> separate_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 5)
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
    """
    result = []
    lst = []
    i = 0
    while i in range(len(d)):
        lst = d[i:i+n]
        result.append(lst)
        i += n
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
