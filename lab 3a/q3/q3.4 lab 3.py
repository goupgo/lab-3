def arrange_string(s):
    lower_case = ''.join([char for char in s if char.islower()])
    upper_case = ''.join([char for char in s if char.isupper()])
    return lower_case + upper_case


str1 = "PyNaTive"


arranged_string = arrange_string(str1)
print(arranged_string)
