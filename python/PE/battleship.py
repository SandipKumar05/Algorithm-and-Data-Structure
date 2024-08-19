# There is a matrix with . and X, where X represents battleship, always of length 3. Battleship can be vertical 
# or horizontal, never diagonal. Given a function bomb_at(i,j), returns True if battleship is present at (i,j) 
# in the matrix. Print the head, middle, tail coordinates of the battleship.

# I asked a question to clarify, and as it turns out there will always be one battleship.

# .........
# .....X...
# .....X...
# .....X...
# .........
def find_battleship(matrix):
  """
  This function finds the battleship in a matrix and prints its coordinates.

  Args:
      matrix: A list of lists representing the matrix (rows and columns).

  Returns:
      None
  """
  rows, cols = len(matrix), len(matrix[0])

  # Iterate through the matrix
  for i in range(rows):
    for j in range(cols):
      # Check if current cell is 'X' and within bounds for a horizontal battleship
      if matrix[i][j] == 'X' and j <= cols - 2:
        # Check if next two cells are also 'X'
        if matrix[i][j + 1] == 'X' and matrix[i][j + 2] == 'X':
          print(f"Battleship found:")
          print(f"Head: ({i}, {j})")
          print(f"Middle: ({i}, {j + 1})")
          print(f"Tail: ({i}, {j + 2})")
          return  # Battleship found, terminate search

      # Check if current cell is 'X' and within bounds for a vertical battleship
      elif matrix[i][j] == 'X' and i <= rows - 2:
        # Check if next two cells below are also 'X'
        if matrix[i + 1][j] == 'X' and matrix[i + 2][j] == 'X':
          print(f"Battleship found:")
          print(f"Head: ({i}, {j})")
          print(f"Middle: ({i + 1}, {j})")
          print(f"Tail: ({i + 2}, {j})")
          return  # Battleship found, terminate search

  # If loop completes without finding a battleship, print a message
  print("Battleship not found in the matrix.")

# Example usage (replace the matrix with your actual data)
matrix = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
]
find_battleship(matrix)
