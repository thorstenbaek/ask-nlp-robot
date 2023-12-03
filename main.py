from fastapi import FastAPI
from utils import loader
from pydantic import BaseModel

class Query(BaseModel):
    corpus: str

app = FastAPI()
nlp = loader.load_model()
loader.load_ruler(nlp)

@app.get("/")
async def root():
    return "YES!"

@app.post("/ent")
def ent_query(item: Query):
    """Query for entitities in the given attribute corpus. """
    doc = nlp(item.corpus)
    return [
        {"start": ent.start_char, "end": ent.end_char,
         "label": ent.label_, "id": ent.ent_id_, "text": ent.text}
        for ent in doc.ents
    ]