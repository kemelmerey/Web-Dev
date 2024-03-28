def make_chocolate(small, big, goal):
    max_big = goal // 5
    if big >= max_big:
        goal -= max_big * 5
    else:
        goal -= big * 5

    if small >= goal:
        return goal
    else:
        return -1