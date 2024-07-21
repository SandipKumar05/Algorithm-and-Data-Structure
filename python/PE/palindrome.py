def is_palindrome_loop(text):
  """
  Checks if a string is a palindrome using a loop and two pointers.

  Args:
      text: The string to check.

  Returns:
      bool: True if the string is a palindrome, False otherwise.
  """
  text = text.lower().casefold()
  left, right = 0, len(text) - 1

  while left < right:
    if text[left] != text[right]:
      return False
    left += 1
    right -= 1

  return True

# Example usage (same as previous)
def is_palindrome(text):
  """
  Checks if a string is a palindrome (reads the same backward as forward).

  Args:
      text: The string to check.

  Returns:
      bool: True if the string is a palindrome, False otherwise.
  """
  return text.lower().casefold() == text[::-1]

# Example usage
text = "Racecar"
if is_palindrome(text):
  print(f"'{text}' is a palindrome.")
else:
  print(f"'{text}' is not a palindrome.")

# Case-insensitive and punctuation handling
text = "A man, a plan, a canal: Panama"
if is_palindrome(text):
  print(f"'{text}' (case-insensitive) is a palindrome.")
else:
  print(f"'{text}' (case-insensitive) is not a palindrome.")
