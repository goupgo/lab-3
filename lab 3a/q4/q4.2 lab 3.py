import string

def remove_punctuation(s):
    
    translator = str.maketrans('', '', string.punctuation)
    
    return s.translate(translator)


str1 = "/@Jon is &developer & musician"

result = remove_punctuation(str1)
print(result)