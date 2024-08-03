def is_palindrome(word) -> bool:
    cleaned = "".join(only_letters(word)).lower()
    return cleaned == cleaned[::-1]


def only_letters(word):
    return (c for c in word if c.isalpha())
