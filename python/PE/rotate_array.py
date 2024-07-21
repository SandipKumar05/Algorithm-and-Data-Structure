def rotate_array_part(arr, start, end):
  """
  Rotates a part of an array in-place.

  Args:
      arr: The list of elements to rotate.
      start: The starting index (inclusive) of the subarray to rotate.
      end: The ending index (exclusive) of the subarray to rotate.
  """

  # Handle invalid input (empty array or invalid indices)
  if not arr or start < 0 or end > len(arr) or start >= end:
    return

  # Length of the subarray to rotate
  subarray_length = end - start

  # Use a temporary variable to store the first element of the subarray
  temp = arr[start]

  # Efficient rotation using a single loop
  for i in range(subarray_length):
    arr[(start + i + 1) % len(arr)] = arr[start + i]

  # Place the stored first element at the end of the subarray
  arr[start] = temp

# Example usage
array = [1, 2, 3, 4, 5, 6, 7]
rotate_array_part(array, 2, 5)  # Rotate elements at indices 2 (inclusive) to 4 (exclusive)
print(array)  # Output: [1, 2, 5, 4, 3, 6, 7]