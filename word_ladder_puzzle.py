from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

        # TODO
        # implement __eq__ and __str__
        # __repr__ is up to you
    def __eq__(self, other):
        """
        Return whether WordLadderPuzzle self is equivalent to other.

        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle | Any
        @rtype: bool
        
        >>> ws = {'cost', 'cat', 'cast', 'case', 'word', 'cave', 'save', 'money', 'party', 'same'}
        >>> w1 = WordLadderPuzzle("same", "cost", ws)
        >>> w2 = WordLadderPuzzle("same", "cost", ws)
        >>> w1.__eq__(w2)
        True
        >>> w3 = WordLadderPuzzle("save", "cost", ws)
        >>> w1.__eq__(w3)
        False
        """
        return (type(self) == type(other) and self._from_word == other._from_word and self._to_word == other._to_word and self._word_set == other._word_set)
    
    def __str__(self):
        """
        Return a human-readable string representation of WordLadderPuzzle self.
        
        >>> ws = {'cost', 'cat', 'cast', 'case', 'word', 'cave', 'save', 'money', 'party', 'same'}
        >>> w1 = WordLadderPuzzle("same", "cost", ws)        
        >>> w1.__str__()
        'same -> cost'
        """    
        return ("{} -> {}".format(self._from_word, self._to_word))
    
        # TODO
        # override extensions
        # legal extensions are WordLadderPuzzles that have a from_word that can
        # be reached from this one by changing a single letter to one of those
        # in self._chars
    def extensions(self):
        """
        Return list of extensions of WordLadderPuzzle self.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]
        
        >>> ws = {'cost', 'cat', 'cast', 'case', 'word', 'cave', 'save', 'money', 'party', 'same', 'most', 'some', 'came'}
        >>> w1 = WordLadderPuzzle("same", "cost", ws) 
        >>> L1 = w1.extensions()
        >>> w2 = WordLadderPuzzle("some", "cost", ws) 
        >>> w3 = WordLadderPuzzle("save", "cost", ws)
        >>> w4 = WordLadderPuzzle("came", "cost", ws) 
        >>> L2 = [w2, w3, w4]
        >>> len(L1) == len(L2)
        True
        """  
        new = ''
        result = []
        ws = self._word_set.copy()
        ws.remove(self._from_word)        
        for i in range(len(self._from_word)):
            for char in self._chars:  
                new = self._from_word[:i] + char + self._from_word[i+1:]
                for word in ws:
                    if len(word) == len(self._from_word) and word == new:
                        result.append(WordLadderPuzzle(new, self._to_word, ws))
        return result        

        # TODO
        # override is_solved
        # this WordLadderPuzzle is solved when _from_word is the same as
        # _to_word
    def is_solved(self):
        """
        Return whether WordLadderPuzzle self is solved.

        @type self: WordLadderPuzzle
        @rtype: bool  
        
        >>> ws = {'cost', 'cat', 'cast', 'case', 'word', 'cave', 'save', 'money', 'party', 'same', 'most'}
        >>> w1 = WordLadderPuzzle("same", "cost", ws) 
        >>> w1.is_solved()
        False
        >>> w2 = WordLadderPuzzle("cost", "cost", ws)
        >>> w2.is_solved()
        True
        """ 
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()

    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))

    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()