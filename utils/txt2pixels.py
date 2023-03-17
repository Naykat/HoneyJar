#Text to pixels utilities
from PIL import Image
from math import ceil

def calculate_image_size(text: str) -> tuple:
    if len(text)<=12:
        return 4,3
    else:
        y = int((len(text)/4*3)**0.5)
        x = ceil(y/3)*4
        if x*y>=len(text):
            return x,y
        else:
            while x*y<len(text):
                y+=1
            return x,y
        
    
def from_letter_to_rgb(letter: chr) -> tuple:
    letter = ord(letter)+1
    return letter%255, letter//255, 255-letter%255 

def get_current_pixel_position(index: int, width: int) -> tuple:
    x = index%width
    y = index//width
    return x, y

def decode_pixel(pixel: tuple):
    if pixel == (0,0,0):
        return ""
    r,g = pixel[:2]
    return chr(g*255+r-1)
