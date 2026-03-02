def simpleCipher(encrypted, k):
    k = k % 26
    decrypted = ""

    for char in encrypted:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            new_index = (index - k) % 26
            decrypted += chr(new_index + ord('A'))
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            new_index = (index - k) % 26
            decrypted += chr(new_index + ord('a'))
        else:
            decrypted += char

    return decrypted
