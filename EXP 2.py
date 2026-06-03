def ends_with_ab(string):
    state = 0

    for char in string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0

    return state == 2

test_strings = ["ab", "aab", "aaab", "abab", "aba", "abb"]

for s in test_strings:
    if ends_with_ab(s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")
