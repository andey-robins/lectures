def decrypt(cipher_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for alpha_character in alphabet:
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

        shift = ord(maxKey) - ord(alpha_character)

        plain_text = ""
        for letter in cipher_text:
            if letter.isalpha():
                plain_text_ord = ord(letter) - shift

                offset_letter = 'a'
                if letter.isupper():
                    offset_letter = 'A'

                plain_text_ord = (plain_text_ord - ord(offset_letter)) % 26
                plain_text_ord += ord(offset_letter)

                plain_text_letter = chr(plain_text_ord)
                plain_text += plain_text_letter
            else:
                plain_text += letter

        print(plain_text)
        print()


# cipher_text = """
# L pxvw qrw ihdu.
# Ihdu lv wkh plqg-nloohu.
# Ihdu lv wkh olwwoh-ghdwk wkdw eulqjv wrwdo reolwhudwlrq.
# L zloo idfh pb ihdu.
# L zloo shuplw lw wr sdvv ryhu ph dqg wkurxjk ph.
# Dqg zkhq lw kdv jrqh sdvw, L zloo wxuq wkh lqqhu hbh wr vhh lwv sdwk.
# Zkhuh wkh ihdu kdv jrqh wkhuh zloo eh qrwklqj. Rqob L zloo uhpdlq.
# """

cipher_text = """
øéêö  Px vahhlx mh zh mh max fhhg. Px vahhlx mh zh mh max fhhg bg mabl wxvtwx tgw wh max hmaxk mabgzl, ghm uxvtnlx maxr tkx xtlr, unm uxvtnlx maxr tkx atkw, uxvtnlx matm zhte pbee lxkox mh hkztgbsx tgw fxtlnkx max uxlm hy hnk xgxkzbxl tgw ldbeel, uxvtnlx matm vateexgzx bl hgx matm px tkx pbeebgz mh tvvxim, hgx px tkx ngpbeebgz mh ihlmihgx, tgw hgx pabva px bgmxgw mh pbg, tgw max hmaxkl, mhh.
"""

# cipher_text = """
# TTTTeeee.
# """

decrypt(cipher_text)
