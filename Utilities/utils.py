def RaiseTypeError(variable_name: str, necessaryType: str, currentType: str) -> Exception:
    raise TypeError(f'{variable_name} must be {necessaryType}, not {currentType}')

def getType(var) -> str: #Gets the type of variable and returns it as a string
    v = str(type(var))
    pos1 = v.find("'")
    pos2 = v.rfind("'")
    v = v[pos1+1:pos2]
    return v

def bSet(var: str or list) -> str or list: #Analogue to set(), but saves the order
    if type(var) is str:
        clean_string = ''
        for letter in var:
            if not(letter in clean_string):
                clean_string+=letter
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

def fingCharPosition(string: str) -> str: 
    digits = '0123456789'
    letter = 0
    while string[letter] in digits:
        letter+=1
    return string[:letter+1]

def createArrayWithDividedEncodedLetters(string: str) -> list: 
    array= []
    for string_with_letter_positions in range(string.count(' ')):
        array.append(string[:string.find(' ')])
        string = string[string.find(' ')+1:]
    return array

def returnChar(dictionary: dict, pos: int, alphabet: str) -> str:
    for letter in alphabet:
        if pos in dictionary[letter]:
            char = letter
            break    
    return char        

def calculateFullStringLength(dictionary: dict, alphabet: str) -> int:
    amount = 0
    for letter in alphabet:
        amount+=len(dictionary[letter])
    return amount

def swap_string(string: str, swap: int) -> list:
  array = []
  for split in range(0,len(string),swap):
    array.append(string[:swap])
    string = string[swap:]
  return array

def swap_letters(string: str):
  if len(string)==1:
    return string
  else:
    return string[-1]+string[1:-1]+string[0]
            


            
