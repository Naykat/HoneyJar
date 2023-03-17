#SPoL utilities
def swap_string(string: str, swap_step: int) -> list:
  array = []
  for gap in range(0,len(string),swap_step):
    array.append(string[:swap_step])
    string = string[swap_step:]
  return array

def swap_letters(string: str):
  if len(string)==1:
    return string
  else:
    return string[-1]+string[1:-1]+string[0]
