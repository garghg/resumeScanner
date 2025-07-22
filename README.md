# Resume Scanner
You can upload your resume and paste a job description. The application will use NLP to give you a score on how well your resume matches the job description. It will also use a custom trained NER model to extract skills from both the resume and job. Finally, it will compare them and suggest skills and keywords to add to your resume.  

<img width="1919" height="959" alt="image" src="https://github.com/user-attachments/assets/cf4509f7-c79b-40f4-a710-7909bf97bba6" />
<img width="1918" height="990" alt="image" src="https://github.com/user-attachments/assets/25c1f1ce-2407-4462-84aa-4edb773befe9" />


---
## Set Up

1. Run `pip install -r requirements.txt` to install all dependencies
2. Run `python main.py`

_Please note:_
- _The model's outputs may occasionally contain inaccuracies or unexpected results._  
- _Please also run model.py to train your custom NER model if you find issue with main.py or running the uploaded model. It may take several minutes to train._

