
"""
with open(path_to_file) as f:
    file_contents = f.read()
print(file_contents)
"""
path_to_file = "books/frankenstein.txt"
def WordCounter():
    
    count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
    #replaced = file_contents.replace("--"," ")
    count = len(replaced.split())
    return count
def CharCounter():
    count = 0
    countCharacters = {
        'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,
        'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,
        'm': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,
        's': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,
        'y': 0,'z': 0
        }
    with open(path_to_file) as f:
        file_contents = f.read()
    lowerCase = file_contents.lower()
    for char in lowerCase:
        if char in countCharacters:
            countCharacters[char] += 1

    return countCharacters


print(CharCounter())