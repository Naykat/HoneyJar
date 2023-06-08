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
### RSA
**_class_ RSA** takes **p** and **q** as an argument. Type: _int_
**p** _and_ **q** _must be prime numbers!_
1) **encode** *— encrypts text*
2) **decode** *— decrypts text*
3) **get_private_key** *— returns private key*
4) **get_public_key** *— returns public key*
### VCI
**_class_ VCI** takes **key** as an argument. Type: _str_
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
encryption2 = SPoL()
def encryption2_encode(text: str) -> str:
    return encryption2.encode(text)
def encryption2_decode(text: str) -> str:
    return encryption2.decode(text)
    
#RSA
encryption3 = RSA(3557, 2579)
def encryption3_public_key() -> tuple:
    return encryption3.get_public_key()
def encryption3_private_key() -> tuple:
    return encryption3.get_private_key()
def encryption3_encode(text: str) -> str:
    return encryption3.encode(encryption3_public_key(), text)
def encryption3_decode(text: str) -> str:
    return encryption3.decode(encryption3_private_key(), text)

#LtLC
encryption4 = LtLC()
def encryption4_encode(text: str) -> str:
    return encryption3.encode(text)
def encryption4_decode(text: str) -> str:
    return encryption4.decode(text)

#VCI
encryption5 = VCI("HONEYJAR")
def encryption5_encode(text: str) -> str:
    return encryption5.encode(text)
def encryption5_decode(text: str) -> str:
    return encryption5.decode(text)

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
