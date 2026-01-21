from sentence_transformers import SentenceTransformer, util
from utils.syllabus import UPSC_SYLLABUS

model = SentenceTransformer('all-MiniLM-L6-v2') # model used to compute text embeddings

def classify(article):
    labels = []
    article_vec = model.encode(article, convert_to_tensor=True)

    for topic, keywords in UPSC_SYLLABUS.items():
        topic_text = topic + " " + " ".join(keywords)
        topic_vec = model.encode(topic_text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(article_vec, topic_vec).item()
        print("SCORE", topic, round(score, 2))

        if score > 0.3:
            labels.append(topic)
    return labels

# def is_relevant(article):
#     syllabus_text = []
#     for topic, words in UPSC_SYLLABUS.items():
#         syllabus_text.append(f"{topic}: " + ", ".join(words))

#     article_vec = model.encode(article, convert_to_tensor=True)
#     syllabus_vec = model.encode(syllabus_text, convert_to_tensor=True) 


#     scores = util.pytorch_cos_sim(article_vec, syllabus_vec)
#     return scores.max().item() > 0.25


