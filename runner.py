"""runner module for testion the codes"""

from PIL import Image
from pic_to_table.table_extraction import DetectTable as DT
from pic_to_table.table_structure_recognition import RecognizeTableStructure as RTS

DETECT_TABLE = DT(input_image=Image.open('Sample table.png').convert('RGB')).detect_table()

def get_cropped_table(image: Image) -> Image:
    """method to get cropped image on table"""

    if len(DETECT_TABLE) == 1:
        cropped_img = image.crop(DETECT_TABLE[0])
        return cropped_img


if __name__ == "__main__":
    sample_image = Image.open('Sample table.png').convert('RGB')
    recognised_ = RTS(get_cropped_table(sample_image).convert('RGB')).recognize_structure()
    columns = [column[1] for column in recognised_ if column[0] == 'table column']
