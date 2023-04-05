def decrypt(cipher_text):
    cipher_text = cipher_text.lower()
    # with a for loop
    frequency = {}
    for letter in cipher_text:
        if letter.isalpha():
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1

    maxVal = 0
    maxKey = ""
    for key, val in frequency.items():
        if val > maxVal:
            maxVal = val
            maxKey = key

    shift = ord(maxKey) - ord('e')

    plain_text = ""
    for letter in cipher_text:
        if letter.isalpha():
            plain_text_ord = ord(letter) - shift
            plain_text_letter = chr(plain_text_ord)
            plain_text += plain_text_letter
        else:
            plain_text += letter

    return plain_text


cipher_text = """
L pxvw qrw ihdu.
Ihdu lv wkh plqg-nloohu.
Ihdu lv wkh olwwoh-ghdwk wkdw eulqjv wrwdo reolwhudwlrq.
L zloo idfh pb ihdu.
L zloo shuplw lw wr sdvv ryhu ph dqg wkurxjk ph.
Dqg zkhq lw kdv jrqh sdvw, L zloo wxuq wkh lqqhu hbh wr vhh lwv sdwk.
Zkhuh wkh ihdu kdv jrqh wkhuh zloo eh qrwklqj. Rqob L zloo uhpdlq.
"""

print(decrypt(cipher_text))
