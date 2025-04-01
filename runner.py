"""runner module for testion the codes"""

from PIL import Image
from pic_to_table.table_extraction import DetectTable as DT

detect_table = DT(input_image=Image.open('Sample table.png').convert('RGB')).visualize_image()
