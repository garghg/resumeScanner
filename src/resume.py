#import necessary modules
import fitz
import spacy
from sentence_transformers import SentenceTransformer
import os
import gdown
import zipfile

#get my custom trained model from google drive (OR you may choose to train you own and load it)
MODEL_DIR = "resume_model"
MODEL_ZIP = "resume_model.zip"
MODEL_URL = "https://drive.google.com/file/d/1q1QL_jVzp87PtNpR426w-hsqqVReshx_/view?usp=sharing"

if not os.path.exists(MODEL_DIR):
    gdown.download(MODEL_URL, MODEL_ZIP, quiet=False)
    with zipfile.ZipFile(MODEL_ZIP, 'r') as zip_ref:
        zip_ref.extractall(MODEL_DIR)

nlp = spacy.load(MODEL_DIR)

resume_skills = []
job_skills = []

def getSkills(texts):
    for index, text in enumerate(texts):
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        [resume_skills.append(ent[0]) for ent in entities if index == 0]
        [job_skills.append(ent[0]) for ent in entities if index == 1]
        skills_needed = [skill for skill in job_skills if skill not in resume_skills]
    return skills_needed



#get sentence transformers model to use
model = SentenceTransformer("all-MiniLM-L6-v2")


def compare(resume, job):
    #open resume as a readable pymupdf doc
    doc = fitz.open(resume)
    #iterate over doc and get resume text from each page
    resume_text = ''
    for page in doc:
        resume_text += page.get_text()
    #clean up enters and spaces from job description
    job = ' '.join(job.split())
    #pass resume text and job text in model as a list
    texts = [resume_text, job]
    #pass texts into NLP model
    skills_needed = getSkills(texts)
    #create embeddings to check similarities
    embeddings = model.encode(texts)
    similarities = model.similarity(embeddings, embeddings)
    #convert similarity score to a percentage
    score = round(similarities.tolist()[0][1], 4)*100
    #return score as a string
    return str(score), skills_needed
