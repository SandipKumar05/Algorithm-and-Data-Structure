def findFaultyCheckin(checkins):
    """
    Perform a binary search to find the first faulty check-in.
    
    Parameters:
    checkins (list): A list of check-ins (or commit IDs) sorted in the order they were made.
    
    Returns:
    int: The index of the first faulty check-in.
    """
    
    def isFaulty(checkin):
        # This is a mock function. In reality, you would have a way to check
        # if a given check-in is faulty.
        pass
    
    left = 0
    right = len(checkins) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if isFaulty(checkins[mid]):
            # Fault found, but continue checking to find the first one
            right = mid
        else:
            # The fault lies further in the branch
            left = mid + 1
    
    return left if isFaulty(checkins[left]) else -1

# Example usage:
checkins = [1, 2, 3, 4, 5, 6, 7, 8]  # Assume check-ins are represented by IDs
# Assume that the fault was introduced in check-in 5
findFaultyCheckin(checkins)
