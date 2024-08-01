#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """

    if not boxes:
        return False

    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys_to_try = boxes[0]

    while keys_to_try:
        key = keys_to_try.pop(0)
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True
            keys_to_try.extend(boxes[key])

            return all(unlocked)
