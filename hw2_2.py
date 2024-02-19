from collections import deque


def is_palindrome(input_string):
    input_string = input_string.lower().replace(' ', '')

    d = deque(input_string)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


print(is_palindrome("Козак з казок"))
