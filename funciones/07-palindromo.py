def proof(text):
    result = False
    clen_text = text.replace(" ", "").lower()
    indice = len(clen_text)
    for a in clen_text:
        indice -= 1
        if a == clen_text[indice]:
            result = True
        else:
            break
    return result


print("Es palindromo", proof("amo la paloma"))
