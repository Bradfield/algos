
def num_paths(height, width):
    if height == 0 or width == 0:
        return 1
    return num_paths(height, width - 1) + num_paths(height - 1, width)
