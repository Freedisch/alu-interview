#!/usr/bin/python3

"""Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains."""


def rain(walls):
    left, right = 0, len(walls) - 1
    left_max = right_max = total_water = 0

    while left <= right:
        if walls[left] <= walls[right]:
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total_water += left_max - walls[left]
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total_water += right_max - walls[right]
            right -= 1

    return total_water
