def create_new_string(s1, s2):
    
    def get_fml(s):
        first = s[0]
        middle = s[len(s) // 2]
        last = s[-1]
        
        if len(s) % 2 == 0:
            middle = s[len(s) // 2 - 1]
        return first + middle + last

    
    return get_fml(s1) + get_fml(s2)


s1 = "America"
s2 = "Japan"


new_string = create_new_string(s1, s2)
print(new_string)