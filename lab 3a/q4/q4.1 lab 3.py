def remove_non_integers(s):
    
    filtered_characters = [char for char in s if char.isdigit()]
    
    return ''.join(filtered_characters)


str1 = "I am 25 years and 10 months old"

filtered_string = remove_non_integers(str1)
print(filtered_string)
