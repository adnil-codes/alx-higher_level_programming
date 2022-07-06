#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    num_list = [roman[char] for char in s]
    length = len(num_list)
    for i in range(length):
        if i < length-1 and num_list[i] < num_list[i+1]:
            res -= num_list[i]
        else:
            res += num_list[i]
    return (res)
