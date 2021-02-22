from ColorPair import get_total_major_colors as major_len
from ColorPair import get_total_minor_colors as minor_len 
import ColorPairGenerator as cpg

def createReferenceData():
    pair_number_start_index = 1
    pair_number_end_index = major_len()*minor_len() + 1     
    reference_data = []
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        major_color, minor_color = cpg.get_color_from_pair_number(pair_number)
        formatted_colorpair = cpg.color_pair_to_string(major_color, minor_color)
        reference_data.append({'Pair Number': pair_number, 'Color Code pairs': formatted_colorpair})
    return reference_data

def printTable(refData, colList=None):
    if not colList: colList = list(refData[0].keys() if refData else [])
    myList = [colList] # 1st row = header
    for item in refData: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
    colSize = [max(map(len,col)) for col in zip(*myList)]
    formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
    myList.insert(1, ['-' * i for i in colSize]) # Seperating line
    for item in myList: print(formatStr.format(*item))
    