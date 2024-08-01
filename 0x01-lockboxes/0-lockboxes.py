#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list): A list of lists representing the keys in each box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is unlocked
    keys_to_try = boxes[0]  # Start with the keys in the first box

    while keys_to_try:
        key = keys_to_try.pop(0)  # Get the next key
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True  # Unlock the box
            keys_to_try.extend(boxes[key])

    return all(unlocked)  # Return True, False otherwise