from fastapi import FastAPI, Request
from pydantic import BaseModel
from lemmatization import lemmitize

class Req(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "up"}

@app.post("/lemmas")
async def get_lemmas(request: Request):
    body_bytes = await request.body()
    content = body_bytes.decode('utf-8')
    lemmas = lemmitize(content)
    return lemmas
