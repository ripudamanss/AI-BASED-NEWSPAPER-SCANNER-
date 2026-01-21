from sentence_transformers import SentenceTransformer, util
from utils.syllabus import UPSC_SYLLABUS

model = SentenceTransformer('all-MiniLM-L6-v2')

def is_relevant(article):
    syllabus_text = []
    for topic, words in UPSC_SYLLABUS.items():
        syllabus_text.append(f"{topic}: " + ", ".join(words))

    article_vec = model.encode(article, convert_to_tensor=True)
    syllabus_vec = model.encode(syllabus_text, convert_to_tensor=True) 


    scores = util.pytorch_cos_sim(article_vec, syllabus_vec)
    return scores.max().item() > 0.25


