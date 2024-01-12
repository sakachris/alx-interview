#!/usr/bin/python3
''' module for lockboxes '''


def canUnlockAll(boxes):
    ''' checking if lockboxes can be opened '''
    # Initialize a set to keep track of visited boxes
    visited = set()

    # DFS function to explore the boxes
    def dfs(box_index):
        # Mark the current box as visited
        visited.add(box_index)

        # Explore keys in the current box
        for key in boxes[box_index]:
            # If the key opens a box and the box has not been visited,
            # recursively call DFS
            if key < len(boxes) and key not in visited:
                dfs(key)

    # Start DFS from the first box (boxes[0])
    dfs(0)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
