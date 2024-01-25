from fastapi.responses import HTMLResponse
import spacy
from fastapi import FastAPI
from spacy import displacy
app = FastAPI()
nlp = spacy.load("fr_dep_news_trf")
@app.get("/", response_class=HTMLResponse)
async def root():
    return "Bienvenue hehehe!"

@app.get("/visualize/{text}", response_class=HTMLResponse)
async def visualize_dep(text: str):
    doc = nlp(text)
    html = displacy.render(doc, style="dep")
    return HTMLResponse(content=html)



@app.post("/tokenize")
async def tokenize(text: str):
    doc = nlp(text) 
    return {
        "tokens": [
            {
                "text": token.text,
                "lemma": token.lemma_,
                "pos": token.pos_,
                "tag": token.tag_,
                "dep": token.dep_,
                "head": token.head.text,
                "head_morf": token.head.morph.to_dict(),
                "morph": token.morph.to_dict(),

            }
            for token in doc
        ],
    }
