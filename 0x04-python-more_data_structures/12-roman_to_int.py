#!/usr/bin/python3
def roman_to_int(roman):
    if not roman:
        return 0
    if not isinstance(roman, str):
        return 0
    if not roman.isupper():
        return 0

    r_dict = {
        "1": 1,
	"IV": 4,
	"V": 5,
	"IX": 9,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000
    }

    result = 0
    temp = list(roman)
    if len(temp) > 1:
        idx = 0
        for i in temp:
            try:
                if temp[idx] == 'I' and temp[idx + 1] == 'V':
                    temp[idx:idx + 2] = [''.join(temp[idx:idx + 2])]
            except IndexError:
                pass
            try:
                if temp[idx] == 'I' and temp[idx + 1] == 'X':
                    temp[idx:idx + 2] = [''.join(temp[idx:idx + 2])]
            except IndexError:
                pass
            idx += 1
    for k, v in r_dict.items():
        for index in temp:
            if index == k:
                result += v
    return result
