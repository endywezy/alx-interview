#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = set(boxes[0])
    unlocked = {0}

    while True:
        added = False
        for i, box in enumerate(boxes):
            if i in unlocked and i not in keys:
                keys.update(box)
                unlocked.update(box)
                added = True
        if not added:
            break

    return len(unlocked) == len(boxes)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))
    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))
    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))