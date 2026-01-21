import re

def split_articles(text):
    #Split by big headlines or section breaks
    parts = re.split(r"\n[A-Z][A-Za-z ,’'–\-]{10,}\n", text)
    clean = []

    for p in parts:
        p = p.strip()
        if len(p) > 300: # Ignore very short parts
            clean.append(p)

    return clean