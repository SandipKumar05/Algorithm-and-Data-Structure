## Fizzbuzz
# for n in range(101):
#     if n%3 == 0 and n%5 == 0:
#         print("FizzBuzz")
#     elif n%3 == 0:
#         print("Fizz")
#     elif n%5 == 0:
#         print("Buzz")
#     else:
#         print(n)

# palindrome check
def check(s):
    if s.lower() == s.lower()[::-1]:
        return True
    return False
print(check('Radar'))