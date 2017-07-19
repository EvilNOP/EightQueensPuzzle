def conflict(state, nextX):
    """
    Given the positions of the queens(in the form of a state of tuple)
    and determines if position for the next queen generate any conflicts
    """
    nextY = len(state)
    
    for i in range(nextY):
        """
        It is true if the horizontal distance between the next queen and
        the previous one under consideration is either zero(same column)
        or equal to the vitical distance(on a diagonal)
        """
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
            
    return False
