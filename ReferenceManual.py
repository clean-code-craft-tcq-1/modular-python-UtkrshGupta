from ColorPair import get_total_major_colors as major_len
from ColorPair import get_total_minor_colors as minor_len 
import ColorPairGenerator as cpg

from tabulate import tabulate 


def createReferenceData():
    pair_number_start_index = 1
    pair_number_end_index = major_len()*minor_len() + 1     
    reference_data = []
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        major_color, minor_color = cpg.get_color_from_pair_number(pair_number)
        formatted_colorpair = cpg.color_pair_to_string(major_color, minor_color)
        reference_data.append([pair_number,formatted_colorpair])
    return tabulate(reference_data, headers=['Pair Number', 'Color Pair'], tablefmt='github')
