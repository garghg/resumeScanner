#import necessary modules
import fitz
import spacy
from sentence_transformers import SentenceTransformer
import os
import gdown
import zipfile

MODEL_DIR = "resume_model"
MODEL_ZIP = "resume_model.zip"
MODEL_ID = "1q1QL_jVzp87PtNpR426w-hsqqVReshx_"

if not os.path.exists(MODEL_DIR):
    print("Downloading model...")
    gdown.download(id=MODEL_ID, output=MODEL_ZIP, quiet=False)
    print("Extracting model...")
    with zipfile.ZipFile(MODEL_ZIP, 'r') as zip_ref:
        zip_ref.extractall(MODEL_DIR)

print("Loading model...")
nlp = spacy.load(MODEL_DIR)
print("Model loaded successfully")


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
