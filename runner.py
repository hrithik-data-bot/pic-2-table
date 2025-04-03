"""runner module for testion the codes"""

from PIL import Image, ImageDraw
from pic_to_table.table_extraction import DetectTable as DT
from pic_to_table.table_structure_recognition import RecognizeTableStructure as RTS

DETECT_TABLE = DT(input_image=Image.open('SampleImage.png').convert('RGB')).detect_table()

def get_cropped_table(image: Image) -> Image:
    """method to get cropped image on table"""

    if len(DETECT_TABLE) == 1:
        cropped_img = image.crop(DETECT_TABLE[0])
        return cropped_img


if __name__ == "__main__":
    sample_image = Image.open('SampleImage.png').convert('RGB')
    cropped_table = get_cropped_table(sample_image).convert('RGB')
    recognised_ = RTS(cropped_table).recognize_structure()
    columns = [col[1] for col in recognised_ if col[0] == 'table column']
    for col in columns:
        current_col = col
        current_col[0]-=10
        current_col[1]-=10
        current_col[2]+=10
        current_col[3]+=10
    draw = ImageDraw.Draw(cropped_table)
    for box in columns:
        draw.rectangle(box, outline="red", width=1)
    cropped_table.save('xyz.png')

