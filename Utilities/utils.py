from random import shuffle

def RaiseTypeError(variable_name: str, necessaryType: str, currentType: str) -> Exception:
    raise TypeError(f'{variable_name} must be {necessaryType}, not {currentType}')

def RaiseValueError(letter: str) -> Exception:
    raise ValueError(f'Key letter "{letter}" does not exist in the alphabet')

def getType(var) -> str: #Gets the type of variable and returns it as a string
    v = str(type(var))
    pos1 = v.find("'")
    pos2 = v.rfind("'")
    v = v[pos1+1:pos2]
    return v

def shuffleString(string: str) -> str: #Shuffles strings randomly
    if not(type(string) is str):
        currentType = getType(string)
        RaiseTypeError('string', 'str', currentType)
    string = list(string)
    shuffle(string)
    string = str(string).strip("[]").replace(' ','').replace(',','').replace("'",'')
    return string

def bSet(var: str or list) -> str or list: #Analogue to set(), but saves the order
    if type(var) is str:
        clean_string = ''
        for letter in range(len(var)):
            if not(var[letter] in clean_string):
                clean_string+=var[letter]
        return clean_string
    elif type(var) is list:
        clean_array = []
        for item in var:
            if not(item in clean_array):
                clean_array.append(item)
        return clean_array
    else:
        currentType = getType(var)
        RaiseTypeError('var', 'str or list', currentType)

def findPos(string: str, alphabet: str) -> int: 
        res = alphabet.find(string[-1])
        rounds = int(string[:-1])
        position = rounds*len(alphabet)+res
        return position

def createStringToDecode(string: str) -> str: 
    digits = '0123456789'
    letter = 0
    while True:
        
        if string[letter] in digits:
            letter+=1
            
        else:
            break
    string_to_decode = string[:letter+1]
    return string_to_decode

def createArrayWithDividedEncodedLetters(string: str) -> list: 
    array = []
    for i in range(string.count(' ')):
        array.append(string[:string.find(' ')])
        string = string[string.find(' ')+1:]
    return array

def getLetter(string: str) -> str:
    return string[0]

def getCharPos(dictionary: dict, pos: int, alphabet: str) -> str:
    char = ''
    for letter in range(len(alphabet)):
        
        if pos in dictionary[alphabet[letter]]:
            char = alphabet[letter]
            break    
    return char        

def getStringLength(dictionary: dict, alphabet: str) -> int:
    amount = 0
    for letter in range(len(alphabet)):
        
        array = dictionary[alphabet[letter]]
        amount+=len(array)
    return amount

            
