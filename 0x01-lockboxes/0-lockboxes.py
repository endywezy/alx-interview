#!/usr/bin/python3


def canUnlockAll(boxes):
    # Initialize the sets
    keys = set()
    opened_boxes = set()

    keys.add(0)
    opened_boxes.add(0)

    while keys:
        current_key = keys.pop()
        if current_key in opened_boxes:
            continue

        opened_boxes.add(current_key)

        for key in boxes[current_key]:
            if key not in opened_boxes:
                keys.add(key)

    return len(opened_boxes) == len(boxes)
