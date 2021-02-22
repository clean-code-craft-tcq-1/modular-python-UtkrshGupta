MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]


def get_major_color_index(major_color):
    return MAJOR_COLORS.index(major_color)

def get_minor_color_index(minor_color):
    return MINOR_COLORS.index(minor_color)

def get_total_major_colors():
    return len(MAJOR_COLORS)

def get_total_minor_colors():
    return len(MINOR_COLORS)

def get_major_color_by_index(major_index):
    return MAJOR_COLORS[major_index]

def get_minor_color_by_index(minor_index):
    return MINOR_COLORS[minor_index]