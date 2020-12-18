#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if type(roman_string) is str and roman_string is not "":
        decode = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        carry = [roman_string[0], 0]
        for c in roman_string:
            if c not in decode:
                return 0
            if carry[0] == c:
                carry[1] += decode[c]
            elif decode[carry[0]] < decode[c]:
                sum -= carry[1]
                carry[0] = c
                carry[1] = decode[c]
            else:
                sum += carry[1]
                carry[0] = c
                carry[1] = decode[c]
        sum += carry[1]
    return sum
