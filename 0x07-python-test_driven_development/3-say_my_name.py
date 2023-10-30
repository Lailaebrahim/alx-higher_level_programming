#!/usr/bin/python3
"""Module for say_my_name method."""


def say_my_name(first_name, last_name=""):
    """Method for printing My name is {first_name} {last_name}.

    Args:
        first_name: first name string.
        last_name: last name string.

    Raises:
        TypeError: If first_name or last_name are not strings.
        >>> say_my_name("hello", "") #doctest: +REPORT_NDIFF
        My name is hello
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
