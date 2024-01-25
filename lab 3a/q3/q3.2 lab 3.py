def append_in_middle(s1, s2):
    
    middle_index = len(s1) // 2
    
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3


s1 = "Aut"
s2 = "Kelly"

s3 = append_in_middle(s1, s2)
print(s3)
