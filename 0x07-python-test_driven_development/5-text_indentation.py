#!/usr/bin/python3
"""Define a text indentation function"""


def text_indentation(text):
    """Print text with two new lines after each '.''?'':'

    Args:
        text(str) - the string to indent

    Raises:
           TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        print("{}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
