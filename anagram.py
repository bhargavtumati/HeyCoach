def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Sort the characters of both strings and compare
    return sorted(s1) == sorted(s2)


print(is_anagram("hello", "bello"))  # False


