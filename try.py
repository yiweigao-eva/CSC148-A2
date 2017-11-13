from mn_puzzle import MNPuzzle 
from collections import deque

def dfs_lst(puzzle):
    """
    Return the solution path in a list.
    """
    if not puzzle:
        print('None')
        return []
    elif puzzle.fail_fast():
        print('fail')
        return []
    elif puzzle.is_solved():
        print('solved')
        return [puzzle]
 
    else:
        lst = []
        d = deque()
        new = None
        for possible in puzzle.extensions():
            d.append(possible)
        while len(d) != 0:
            new = d.popleft()
            for x in new.extensions():
                if puzzle != x:
                    d.append(x)
            print('r start')
            lst += dfs_lst(new)
            print('r end')
        return lst
def dfs(puzzle):
    
    if not puzzle:
        print('None')
        return None
    elif puzzle.fail_fast():
        print('fail')
        return None
    elif puzzle.is_solved():
        print('is sovled')
        return PuzzleNode(puzzle)
    else:
        check_dq = deque()
        parent = PuzzleNode(puzzle)
        extension = puzzle.extensions()
        past_puzzle = [puzzle]
        for p in extension:
            check_dq.append(PuzzleNode(p, [], parent))
        current_puzzle = check_dq.popleft()
        while not(current_puzzle.puzzle.is_solved()) or len(check_dq) != 0:
            if not(current_puzzle.puzzle.fail_fast()):
                extra_extension = current_puzzle.puzzle.extensions()
                for p in extra_extension:
                    if not(p in past_puzzle):
                        check_dq.appendleft(PuzzleNode(p, [], current_puzzle))
                past_puzzle.append(current_puzzle.puzzle)

            if check_dq:
                current_puzzle = check_dq.popleft()

        if len(check_dq) == 0:
            return None
        else:
            while current_puzzle.parent is not None:
                current_puzzle.parent.children = [current_puzzle]
                current_puzzle = current_puzzle.parent
            return current_puzzle