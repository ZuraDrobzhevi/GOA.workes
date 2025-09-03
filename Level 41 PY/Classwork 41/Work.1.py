

# name of mission: Is it a palindrome?


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]