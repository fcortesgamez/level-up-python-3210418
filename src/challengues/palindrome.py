import re


def is_palindrome(word) -> bool:
    forwards = "".join(re.findall(r"[a-z]+", word.lower()))
    backwards = forwards[::-1]
    return forwards == backwards
