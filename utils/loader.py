import spacy
import spacy.pipeline

def load_model(model="nb_core_news_sm"): 
    return spacy.load(model)

def load_ruler(nlp, rulerFile='./combined.jsonl'): 
    ruler = nlp.add_pipe("entity_ruler")           
    ruler.from_disk(rulerFile) 
    add_patterns(ruler)

def add_patterns(ruler): 
    patterns = [
        {"label": "LATERALITET", "pattern": "venstre", "id": "SIN"},
        {"label": "LATERALITET", "pattern": "høyre", "id": "DXT"},        
        {"label": "OBSERVATION", "pattern": "BP", "id": "BLOOD_PRESSURE"},
        {"label": "OBSERVATION", "pattern": "BT", "id": "BLOOD_PRESSURE"},
        {"label": "OBSERVATION", "pattern": "puls", "id": "PULSE"},
        {"label": "OBSERVATION", "pattern": "Puls", "id": "PULSE"},
        {"label": "OBSERVATION", "pattern": "resp", "id": "RESP"},
        {"label": "OBSERVATION", "pattern": "Resp", "id": "RESP"},
        {"label": "OBSERVATION", "pattern": "temp", "id": "BODY_TEMP"},
        {"label": "OBSERVATION", "pattern": "Temp", "id": "BODY_TEMP"},
        {"label": "OBSERVATION", "pattern": "temperatur", "id": "BODY_TEMP"},
        {"label": "OBSERVATION", "pattern": "Temperatur", "id": "BODY_TEMP"},

        {"label": "LAB", "pattern": "hb", "id": "HB"},
        {"label": "LAB", "pattern": "Hb", "id": "HB"},
        {"label": "LAB", "pattern": "CRP", "id": "CRB"},

        {"label": "UNIT", "pattern": "C", "id": "CEL"},
        {"label": "UNIT", "pattern": "mmHg", "id": "MMHG"}

    ]
    print(f"Loading custom patterns of size={len(patterns)}")
    ruler.add_patterns(patterns)    

