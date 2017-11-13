"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# uncomment the next two lines on a unix platform, say CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)


# TODO
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    if not puzzle:
        return None
    elif puzzle.fail_fast():
        return None
    elif puzzle.is_solved():
        return PuzzleNode(puzzle)
    else:
        check_dq = deque()
        parent = PuzzleNode(puzzle)
        extension = puzzle.extensions()
        past_puzzle = [puzzle]
        for puzzle in extension:
            check_dq.append(PuzzleNode(puzzle, [], parent))

        current_puzzle = check_dq[0]
        past_puzzle.append(current_puzzle.puzzle)
        while not(current_puzzle.puzzle.is_solved() or
                  len(check_dq) == 0):
            check_dq.popleft()
            if not(current_puzzle.puzzle.fail_fast()):
                extra_extension = current_puzzle.puzzle.extensions()
                for puzzle in extra_extension:
                    if not(puzzle in past_puzzle):
                        new_node = PuzzleNode(puzzle, [], current_puzzle)
                        check_dq.appendleft(new_node)

            if check_dq:
                current_puzzle = check_dq[0]
                past_puzzle.append(current_puzzle.puzzle)

        if check_dq == 0:
            return None
        else:
            while current_puzzle.parent is not None:
                current_puzzle.parent.children = [current_puzzle]
                current_puzzle = current_puzzle.parent
            return current_puzzle


# TODO
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque

def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    if not puzzle:
        return None
    elif puzzle.fail_fast():
        return None
    elif puzzle.is_solved():
        return PuzzleNode(puzzle)
    else:
        check_dq = deque()
        parent = PuzzleNode(puzzle)
        extension = puzzle.extensions()
        past_puzzle = [puzzle]
        for puzzle in extension:
            check_dq.append(PuzzleNode(puzzle, [], parent))

        current_puzzle = check_dq[0]
        past_puzzle.append(current_puzzle.puzzle)
        while not(current_puzzle.puzzle.is_solved() or
                  len(check_dq) == 0):
            check_dq.popleft()
            if not(current_puzzle.puzzle.fail_fast()):
                extra_extension = current_puzzle.puzzle.extensions()
                for puzzle in extra_extension:
                    if not(puzzle in past_puzzle):
                        past_puzzle.append(puzzle)
                        new_node = PuzzleNode(puzzle, [], current_puzzle)
                        check_dq.append(new_node)

            if check_dq:
                current_puzzle = check_dq[0]

        if check_dq == 0:
            return None
        else:
            while current_puzzle.parent is not None:
                current_puzzle.parent.children = [current_puzzle]
                current_puzzle = current_puzzle.parent
            return current_puzzle


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether PuzzleNode self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))