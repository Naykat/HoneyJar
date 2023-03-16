from Ciphers.AoLR import AoLR
from Ciphers.LtLC import LtLC
from Ciphers.SPoL import SPoL
from Utilities.utils import get_type, calculate_image_size, from_letter_to_rgb, get_current_pixel_position, decode_pixel
from Utilities.constants import default_alphabet
from PIL import Image

class HoneyJar():

    def __init__(self, alphabet: str = default_alphabet) -> None:
        if type(alphabet)!=str:
            raise TypeError(f"alphabet must be str, not {get_type(alphabet)}")
        #Protected variable. Can be called, but not changed outside the class
        self._alphabet = alphabet 

        #Private variables. Cannot be called or changed outside the class
        self.__AoLR = AoLR(self._alphabet)
        self.__LtLC = LtLC(int(len(self._alphabet)**0.5))
        self.__SPoL = SPoL()

    def prepare(self, string: str) -> str:
        if type(string)!=str:
            raise TypeError(f"string must be str, not {get_type(string)}")
        string = self.__AoLR.encode(string)
        string = self.__LtLC.encode(string)
        string = self.__SPoL.encode(string)
        return string
        
    def unbar(self, string: str) -> str:
        if type(string)!=str:
            raise TypeError(f"string must be str, not {get_type(string)}")
        string = self.__SPoL.decode(string)
        string = self.__LtLC.decode(string)
        string = self.__AoLR.decode(string)
        return string

def to_pixels(string: str):
    if type(string)!=str:
        raise TypeError(f"string must be str, not {get_type(string)}")
    width, height = calculate_image_size(string)
    image = Image.new("RGB", (width,height))

    for index, letter in enumerate(string):
        x, y = get_current_pixel_position(index, width)
        image.putpixel((x, y),from_letter_to_rgb(letter))
    return image

def to_string(image: Image):
    if type(image)!=Image.Image:
        raise TypeError(f"image must be Image, not {get_type(image)}")
    index = 0
    string = ""
    width = image.size[0]
    while image.getpixel(get_current_pixel_position(index, width))!=(0,0,0):
        x, y = get_current_pixel_position(index, width)
        current_pixel = image.getpixel((x,y))
        string += decode_pixel(current_pixel)
        index+=1
    return string
