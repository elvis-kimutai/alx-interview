#!/usr/bin/python3
"""
Determines if all the boxes can be unlocked
"""


def canUnlockAll(boxes):
    """Fuction to unlock all boxes"""
    unlocked = [0]

    for box_index, box_elements in enumerate(boxes):
        if not box_elements:
            continue

        for key in box_elements:
            if key < len(boxes) and key != box_index and key not in unlocked:
                unlocked.append(key)

    if len(unlocked) == len(boxes):
        return True
    return False
