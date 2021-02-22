import ColorPair as cp

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  total_major_colors = cp.get_total_major_colors()
  major_index = zero_based_pair_number // total_major_colors
  if major_index >= total_major_colors:
    raise Exception('Major index out of range')
  total_minor_colors = cp.get_total_minor_colors()
  minor_index = zero_based_pair_number % total_minor_colors
  if minor_index >= total_minor_colors:
    raise Exception('Minor index out of range')
  return cp.get_major_color_by_index(major_index), cp.get_minor_color_by_index(minor_index)


def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = cp.get_major_color_index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = cp.get_minor_color_index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * cp.get_total_minor_colors() + minor_index + 1
