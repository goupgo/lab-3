# Function to remove empty strings from a list of strings
def remove_empty_strings(str_list):
    # Filter out empty strings and None values
    return [string for string in str_list if string not in ('', None)]

# Given list with empty strings and None values
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Remove empty strings and None values from the list
filtered_list = remove_empty_strings(str_list)
print(filtered_list)