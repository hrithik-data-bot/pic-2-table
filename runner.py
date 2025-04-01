"""runner module for testion the codes"""

from PIL import Image
from pic_to_table.table_extraction import DetectTable as DT

DETECT_TABLE = DT(input_image=Image.open('Sample table.png').convert('RGB')).detect_table()

def get_cropped_table() -> Image:
    """method to get cropped image on table"""

    if len(DETECT_TABLE) == 1:
        cropped_img = Image.open('Sample table.png').convert('RGB').crop(DETECT_TABLE[0])
        return cropped_img


def extract_features(cropped_image: Image) -> Image:
    """extract the features on cropped table"""

    

if __name__ == "__main__":
    get_cropped_table()
