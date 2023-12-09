#!/usr/bin/python3
"""This script contains a function that
determines if a function can be opened"""


def open_box(box, all_boxes, opened_boxes):
    if len(box) == 0:

        return opened_boxes
    for key in box:
        if key in opened_boxes or key > len(all_boxes) - 1:
            continue
        opened_boxes.append(key)
        opened_boxes = open_box(all_boxes[key], all_boxes, opened_boxes)
    return opened_boxes


def canUnlockAll(boxes):
    """This function takes an array of array(boxes) of
    integers(keys) as parameter and determines if all
    the boxes can be opened
    """
    opened_boxes = [0]
    opened_boxes = open_box(boxes[0], boxes, opened_boxes)

    if len(boxes) != len(opened_boxes):
        return False
    else:
        return True
