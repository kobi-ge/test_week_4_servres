
def fence_encrypt(text: str):
    even_idx = ""
    odd_idx = ""
    for idx, letter in enumerate(text):
        if letter == " ":
            continue
        if not idx % 2:
            even_idx += letter
        else:
            odd_idx += letter
    encrypted = even_idx + odd_idx
    return encrypted

def fence_decrypt(text: str):
    length = len(text)
    half = length / 2
    if length % 2:
        half = length / 2 + 1
    text1 = text[:int(half)]
    text2 = text[int(half):]
    full_text = ""
    for idx in range(len(text2)):
        full_text += text1[idx]
        full_text += text2[idx]
    if length % 2:
        full_text += text1[-1]
    return full_text
