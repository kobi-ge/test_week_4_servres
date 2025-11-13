from encryptions_logic import caesar_logic as caesar
from encryptions_logic import fence_logic as fence
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class CaesarBody(BaseModel):
    text: str
    offset: int
    mode: str

# @app.get("/test")
# def test():
#     return {"msg": "hi from test"}
#
# @app.get("/test/{name}")
# def test_save(name: str):
#     with open("names.txt", "a") as file:
#         file.write(name)
#         return {"msg":"saved user"}

@app.post("/post")
def Caesar_cipher(body: CaesarBody):
    if body.mode in ["encrypt", "decrypt"]:
        return caesar.caesar_encrypt(body.mode, body.offset, body.text)
    else:
        return {"invalid mode"}

@app.get("/fence/encrypt")
def fence_encrypt(text: str):
    encrypted = fence.fence_encrypt(text)
    return {"encrypted_text": encrypted}

@app.post("/fence/decrypt")
def fence_decrypt():
    return {"decrypted":"..."}