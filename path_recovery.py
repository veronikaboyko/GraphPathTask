def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        if current is not None:
            current = previous[current]
    path.append(start)
    path.reverse()
    return path
