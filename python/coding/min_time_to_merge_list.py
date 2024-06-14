import heapq

def minimum_cost_to_merge(elements):
    # Base case: if the list is empty or contains only one element, no cost is needed
    if len(elements) <= 1:
        return 0
    
    # Initialize a min-heap with the elements
    heapq.heapify(elements)
    
    total_cost = 0
    
    # Continue merging until only one element remains in the heap
    while len(elements) > 1:
        # Extract the two smallest elements
        first = heapq.heappop(elements)
        second = heapq.heappop(elements)
        
        # Merge them and calculate the cost
        merge_cost = first + second
        total_cost += merge_cost
        
        # Insert the merged element back into the heap
        heapq.heappush(elements, merge_cost)
    
    return total_cost

# Example usage:
elements = [4, 3, 2, 6]
print("Minimum cost to merge all elements:", minimum_cost_to_merge(elements))  # Output: 29
