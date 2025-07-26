# Resume Scanner
You can upload your resume and paste a job description. The application will use NLP to give you a score on how well your resume matches the job description. It will also use a custom trained NER model to extract skills from both the resume and job. Finally, it will compare them and suggest skills and keywords to add to your resume.  


_Due to some technical issue on git locally, I had to create a second repo. This is a continuation of [resumeReader](https://github.com/garghg/resumeReader). Please check that for past commits._


<img width="1919" height="959" alt="image" src="https://github.com/user-attachments/assets/cf4509f7-c79b-40f4-a710-7909bf97bba6" />
<img width="1918" height="990" alt="image" src="https://github.com/user-attachments/assets/25c1f1ce-2407-4462-84aa-4edb773befe9" />


---
## Set Up
You may download and run the executable file [here](https://drive.google.com/uc?export=download&id=1orAgG91R9jNidgf_25DgJmtx3yabhtaX).

3.  **Clone repo**: `git clone https://github.com/garghg/resumeScanner.git`
4.  Enter the src directory
2. **Create venv**: `python -m venv venv`
3. **Activate venv**: `venv\Scripts\activate`
4. **Install dependencies**: `pip install -r requirements.txt`
   If you have issue with requirements.txt, please run the following:
   1. `pip install flask`
   2. `pip install pymupdf`
   3. `pip install spacy`
   4. `pip install sentence_transformers`
   5. `pip install gdown`
6. **Run project**: `python main.py`
7. **Deactivate venv**: `deactivate`

To use the application, simply upload a resume and paste a job description.
For test purposes, a sample resume is provided in the uploads folder. 

_Please note:_
- _The model's outputs may occasionally contain inaccuracies or unexpected results._  
- _Please also run model.py to train your custom NER model if you find issue with main.py or running the uploaded model. It may take several minutes to train._

