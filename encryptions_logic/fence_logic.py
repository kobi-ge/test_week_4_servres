a = "hello world"
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
