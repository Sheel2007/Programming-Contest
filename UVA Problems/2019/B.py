def caesars_cipher(shift, message):
    encoded_message = ""
    
    for char in message:
        if char == ' ':
            encoded_message += ' '
        else:
            # is complicated so ima try and explain it:
            # ok so the part ord(char) - ord('a') gets the index in the alphabet (ex: c is 2)
            # then we add the shifter value to it and use modulus division in case the shift is greater than 26
            # then we add the ord('a') to ensure when we convert it back it is a lowercase letter (the way python stores characters in numerical values is a little weird)
            # finally we convert the index number back to a character
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encoded_message += shifted_char
    
    return encoded_message

# Read the number of test cases
n = int(input())

# Process each test case
for _ in range(n):
    shift = int(input())
    message = input()
    encoded_message = caesars_cipher(shift, message)
    print(encoded_message)
