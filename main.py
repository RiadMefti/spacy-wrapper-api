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
                "is_stop": token.is_stop,
                "is_alpha": token.is_alpha,
                "is_ascii": token.is_ascii,
                "is_digit": token.is_digit,
                "is_lower": token.is_lower,
                "is_upper": token.is_upper,
                "is_title": token.is_title,
                "is_punct": token.is_punct,
                "is_space": token.is_space,
                "is_bracket": token.is_bracket,
                "is_quote": token.is_quote,
                "is_currency": token.is_currency,
                "like_num": token.like_num,
                "like_url": token.like_url,
                "like_email": token.like_email,
                "is_oov": token.is_oov,
                "is_sent_start": token.is_sent_start,
                "morph": token.morph.to_dict(),
                "ent_type": token.ent_type_,
                "ent_iob": token.ent_iob_,
                "norm": token.norm_,
                "left_edge": token.left_edge.text,
                "right_edge": token.right_edge.text,
                "ent_kb_id": token.ent_kb_id_,
                "ent_id": token.ent_id_,
                "lang_": token.lang_,
            }
            for token in doc
        ],
    }
