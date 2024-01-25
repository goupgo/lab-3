def get_middle_four_chars(s):
    if len(s) % 2 != 0:
        return "String does not have a middle four characters."
    
    middle_index = len(s) // 2
    
    return s[middle_index - 2:middle_index + 2]


original_string1 = "BillDescrtan"
original_string2 = "HoSongHu"


middle_four1 = get_middle_four_chars(original_string1)
middle_four2 = get_middle_four_chars(original_string2)

print(middle_four1, middle_four2)
