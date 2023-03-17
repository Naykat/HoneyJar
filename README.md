# HoneyJar
**HoneyJar** is an encryption that will make your messages or files protected

### AoLR
**_class_ AoLR** takes **alphabet** as an argument. Type: _str_
1) **encode** *— encrypts text*
2) **decode** *— decrypts text*
### SPoL
**_class_ SPoL** takes **limit** as an argument. Type: _int_
1) **encode** *— encrypts text*
2) **decode** *— decrypts text*
### LtLC
**_class_ LtLC** takes **step** as an argument. Type: _int_
1) **encode** *— encrypts text*
2) **decode** *— decrypts text*


### Text to Pixels and back!
1) **to_pixels** *— converts text to pixelated image*
2) **to_string** *— converts pixelated image to text*


## QuickStart
```python
from HoneyJar import *

"""
If you do not enter any value
at cipher creation, it sets
the default value. You can
find it in /bin/default_values
"""
#AoLR
encryption1 = AoLR()
def encryption1_encode(text: str) -> str:
    return encryption1.encode(text)
def encryption1_decode(text: str) -> str:
    return encryption1.decode(text)

#SPoL
encryption2 = AoLR()
def encryption2_encode(text: str) -> str:
    return encryption2.encode(text)
def encryption2_decode(text: str) -> str:
    return encryption2.decode(text)

#LtLC
encryption3 = LtLC()
def encryption3_encode(text: str) -> str:
    return encryption3.encode(text)
def encryption3_decode(text: str) -> str:
    return encryption3.decode(text)


#Text to pixels
image = to_pixels("Honey Jar Encryption")
image.save("images/Honey Jar Encryption.png") #Image preservation
image.show() #Image opening

#Pixels to text
text1 = to_string(image)
text2 = to_string("images/example.png")
print(text1)
print(text2)
```




