def decrypt(cipher_text):
    letter_freq = {}
    for letter in cipher_text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    highest_letter = ""
    highest_letter_count = 0
    for letter, count in letter_freq.items():
        if count > highest_letter_count:
            highest_letter = letter
            highest_letter_count = count

    shift = ord(highest_letter) - ord('e')

    plain_text = ""
    for letter in cipher_text:
        if letter.isalpha():
            if letter == letter.lower():
                plain_text += round_shift(letter, shift, False)
            else:
                plain_text += round_shift(letter, shift, True)
        else:
            plain_text += letter

    return plain_text


def ord_to_letter_num(letter, is_cap):
    letter_ord = ord(letter)
    letter_num = letter_ord - get_offset(is_cap)
    return letter_num


def round_shift(letter, shift, is_cap):
    cipher_num = ord_to_letter_num(letter, is_cap)
    plain_num = (cipher_num - shift) % 26
    return chr(plain_num + get_offset(is_cap))


def get_offset(is_cap):
    if is_cap:
        return 65
    return 97


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
