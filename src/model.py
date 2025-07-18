# Based on tutorial by NeuralNine: https://youtu.be/JIz-hiRrZ2g, and
# spaCy documentation: https://spacy.io/usage/training#training-data
# adapted for resume skill recognition trained on the following dataset

# Dataset reference:
    # @article{decorte2023extreme,
    #   title={Extreme multi-label skill extraction training using large language models},
    #   author={Decorte, Jens-Joris and Verlinden, Severine and Van Hautte, Jeroen and Deleu, Johannes and Develder, Chris and Demeester, Thomas},
    #   journal={arXiv preprint arXiv:2307.10778},
    #   year={2023}
    # }

    # process and turn data into TRAIN_DATA by finding skill in sentence indices
    # train model on this

# import all necessary modules
import random
import spacy
from spacy.util import minibatch, compounding
from spacy.training.example import Example
import pandas as pd
import re


# get data set from Hugging Face
csv = pd.read_csv("hf://datasets/TechWolf/Synthetic-ESCO-skill-sentences/dataset.csv")

#get all sentences in the database in a list to iterate over
sentences = csv['sentence'].tolist()

#get all skills in the database in a list to iterate over
skills = csv['skill'].tolist()

# Prepare and annotate your training data with entities and labels.
TRAIN_DATA = []


#process data to format as spaCy model training data
for sentence, skill in zip(sentences, skills):
    # use regex for case-insensitive search in original sentence
    match = re.search(re.escape(skill), sentence, re.IGNORECASE)
    if match:
        #find the start and end of match(skill)
        start, end = match.span()
        #append to TRAIN_DATA
        TRAIN_DATA.append((sentence, {"entities": [(start, end, "SKILL")]}))

#add some tech specific data to TRAIN_DATA
TECH_DATA = [
    ("Proficient in Python, Java, and C#.", ["Python", "Java", "C#"]),
    ("Expertise with machine learning, deep learning, and AI.", ["machine learning", "deep learning", "AI"]),
    ("Experienced in JavaScript, React, Angular, and Vue.js.", ["JavaScript", "React", "Angular", "Vue.js"]),
    ("Skilled at SQL, NoSQL databases, and data warehousing.", ["SQL", "NoSQL", "data warehousing"]),
    ("Knowledgeable in cloud platforms such as AWS, Azure, and Google Cloud.", ["AWS", "Azure", "Google Cloud"]),
    ("Hands-on experience with Docker, Kubernetes, and Jenkins.", ["Docker", "Kubernetes", "Jenkins"]),
    ("Familiar with Git, SVN, and other version control systems.", ["Git", "SVN"]),
    ("Proficient in HTML, CSS, and Bootstrap.", ["HTML", "CSS", "Bootstrap"]),
    ("Strong background in Agile methodologies and Scrum.", ["Agile", "Scrum"]),
    ("Experience using TensorFlow, PyTorch, and Scikit-learn.", ["TensorFlow", "PyTorch", "Scikit-learn"]),
    ("Working knowledge of REST APIs and GraphQL.", ["REST", "GraphQL"]),
    ("Skilled in data visualization tools like Tableau and Power BI.", ["Tableau", "Power BI"]),
    ("Experienced in software testing using Selenium and JUnit.", ["Selenium", "JUnit"]),
    ("Good understanding of networking protocols such as TCP/IP and HTTP.", ["TCP/IP", "HTTP"]),
    ("Competent in Microsoft Office Suite, including Excel and PowerPoint.", ["Microsoft Office Suite", "Excel", "PowerPoint"]),
    ("Proficient with Linux command line tools like Bash and Zsh.", ["Linux", "Bash", "Zsh"]),
    ("Knowledge of C, C++, and embedded systems development.", ["C", "C++", "embedded systems development"]),
    ("Strong communication and leadership skills.", ["communication", "leadership"]),
    ("Experienced with ERP systems like SAP and Oracle.", ["SAP", "Oracle"]),
    ("Familiarity with big data tools such as Hadoop and Spark.", ["Hadoop", "Spark"]),
    ("Skilled in mobile development with Android and iOS platforms.", ["Android", "iOS"]),
    ("Working knowledge of DevOps tools including Ansible and Chef.", ["Ansible", "Chef"]),
    ("Hands-on experience in UI/UX design using Figma and Adobe XD.", ["UI/UX design", "Figma", "Adobe XD"]),
    ("Proficient at scripting languages like Perl and Ruby.", ["Perl", "Ruby"]),
    ("Experience in blockchain technology and smart contract development.", ["blockchain technology", "smart contract development"]),
    ("Strong analytical skills with experience in Excel and Python.", ["analytical skills", "Excel", "Python"]),
    ("Familiar with Agile and Waterfall project management methodologies.", ["Agile", "Waterfall"]),
    ("Experienced in graphic design using Adobe Photoshop and Illustrator.", ["graphic design", "Adobe Photoshop", "Illustrator"]),
    ("Good knowledge of virtualization technologies such as VMware and Hyper-V.", ["VMware", "Hyper-V"]),
    ("Proficient in SQL querying and database administration.", ["SQL", "querying", "database administration"]),
    ("Experience developing microservices architecture with Spring Boot.", ["microservices architecture", "Spring Boot"]),
    ("Skilled in testing automation using Cypress and TestNG.", ["Cypress", "TestNG"]),
    ("Knowledgeable about container orchestration tools such as OpenShift.", ["OpenShift"]),
    ("Familiar with Python libraries like Pandas, NumPy, and Matplotlib.", ["Python", "Pandas", "NumPy", "Matplotlib"]),
    ("Experience working with message brokers such as Kafka and RabbitMQ.", ["Kafka", "RabbitMQ"]),
    ("Strong background in cybersecurity and ethical hacking.", ["cybersecurity", "ethical hacking"]),
    ("Good knowledge of CRM software like Salesforce and HubSpot.", ["Salesforce", "HubSpot"]),
    ("Proficient in RESTful API development and integration.", ["RESTful API development"]),
    ("Experienced in data engineering with Apache Spark and Hadoop.", ["data engineering", "Apache Spark", "Hadoop"]),
    ("Familiar with automated deployment using CircleCI and Travis CI.", ["CircleCI", "Travis CI"]),
    ("Working knowledge of natural language processing (NLP).", ["natural language processing"]),
    ("Strong problem-solving and critical thinking abilities.", ["problem-solving", "critical thinking"]),
    ("Experienced in serverless computing using AWS Lambda.", ["AWS Lambda"]),
    ("Familiar with data mining techniques and tools.", ["data mining"]),
    ("Proficient in scripting with PowerShell and Bash.", ["PowerShell", "Bash"]),
    ("Hands-on experience with database management systems like MySQL and PostgreSQL.", ["MySQL", "PostgreSQL"]),
    ("Skilled in front-end technologies including HTML5, CSS3, and JavaScript.", ["HTML5", "CSS3", "JavaScript"]),
    ("Knowledgeable in software development lifecycle (SDLC) processes.", ["software development lifecycle"]),
    ("Experience with test-driven development (TDD) methodologies.", ["test-driven development"]),
    ("Familiarity with cloud-native applications and Kubernetes orchestration.", ["cloud-native applications", "Kubernetes orchestration"]),
    ("Proficient in Rust, Go, and Elixir.", ["Rust", "Go", "Elixir"]),
    ("Experienced in data pipelines using Apache Beam and NiFi.", ["data pipelines", "Apache Beam", "NiFi"]),
    ("Knowledgeable in containerization with Docker and Podman.", ["containerization", "Docker", "Podman"]),
    ("Hands-on experience in test automation using Robot Framework.", ["test automation", "Robot Framework"]),
    ("Strong understanding of CI/CD pipelines and GitOps.", ["CI/CD pipelines", "GitOps"]),
    ("Skilled in data cleaning and preprocessing with Pandas.", ["data cleaning", "preprocessing", "Pandas"]),
    ("Experienced in backend frameworks such as Express and Django.", ["backend frameworks", "Express", "Django"]),
    ("Proficient in infrastructure as code tools like Terraform and Pulumi.", ["infrastructure as code", "Terraform", "Pulumi"]),
    ("Working knowledge of real-time data streaming with Apache Flink.", ["real-time data streaming", "Apache Flink"]),
    ("Strong skills in performance testing using LoadRunner.", ["performance testing", "LoadRunner"]),
    ("Familiar with security tools like Nessus and Metasploit.", ["Nessus", "Metasploit"]),
    ("Good experience with version control using Mercurial and GitLab.", ["Mercurial", "GitLab"]),
    ("Skilled at writing shell scripts in Bash and Fish.", ["shell scripts", "Bash", "Fish"]),
    ("Expert in scientific computing with SciPy and SymPy.", ["SciPy", "SymPy"]),
    ("Knowledgeable in ITIL framework and IT service management.", ["ITIL", "IT service management"]),
    ("Hands-on experience using development tools like Xcode and Android Studio.", ["Xcode", "Android Studio"]),
    ("Proficient with big data platforms including Hive and Presto.", ["big data platforms", "Hive", "Presto"]),
    ("Experienced in working with ETL processes using Talend.", ["ETL processes", "Talend"]),
    ("Familiarity with data science libraries like Seaborn and Statsmodels.", ["Seaborn", "Statsmodels"]),
    ("Knowledgeable in software container technologies like LXC.", ["software container technologies", "LXC"]),
    ("Proficient in CAD tools such as AutoCAD and SolidWorks.", ["CAD", "AutoCAD", "SolidWorks"]),
    ("Working with distributed systems and eventual consistency.", ["distributed systems", "eventual consistency"]),
    ("Skilled in using monitoring tools like Prometheus and Grafana.", ["Prometheus", "Grafana"]),
    ("Experienced in frontend frameworks like Ember.js and Svelte.", ["frontend frameworks", "Ember.js", "Svelte"]),
    ("Strong background in NoSQL solutions such as Couchbase and Cassandra.", ["NoSQL solutions", "Couchbase", "Cassandra"]),
    ("Familiar with operating systems including Unix and FreeBSD.", ["operating systems", "Unix", "FreeBSD"]),
    ("Proficient in graph databases like Neo4j and ArangoDB.", ["graph databases", "Neo4j", "ArangoDB"]),
    ("Hands-on experience with Business Intelligence tools like QlikView.", ["Business Intelligence", "QlikView"]),
    ("Skilled in hardware description languages such as VHDL and Verilog.", ["hardware description languages", "VHDL", "Verilog"]),
    ("Experienced in analytics platforms such as Looker and Domo.", ["analytics platforms", "Looker", "Domo"]),
    ("Knowledge of mobile frameworks like Flutter and Ionic.", ["mobile frameworks", "Flutter", "Ionic"]),
    ("Familiar with documentation tools like Confluence and Notion.", ["documentation tools", "Confluence", "Notion"]),
    ("Proficient at CRM and ERP integrations.", ["CRM", "ERP", "integrations"]),
    ("Strong understanding of AI/ML workflows and model deployment.", ["AI/ML workflows", "model deployment"]),
    ("Experienced with logging tools like ELK Stack and Fluentd.", ["ELK Stack", "Fluentd"]),
    ("Working with quantum computing concepts and Qiskit framework.", ["quantum computing", "Qiskit"]),
    ("Proficient in e-commerce platforms like Magento and Shopify.", ["e-commerce platforms", "Magento", "Shopify"]),
    ("Familiarity with scientific visualization using ParaView and VisIt.", ["scientific visualization", "ParaView", "VisIt"]),
    ("Hands-on experience in big data processing with Dask.", ["big data processing", "Dask"]),
    ("Strong problem-solving with decision trees and random forests.", ["problem-solving", "decision trees", "random forests"]),
    ("Knowledgeable in multimedia tools such as Final Cut Pro and DaVinci Resolve.", ["multimedia tools", "Final Cut Pro", "DaVinci Resolve"]),
    ("Experienced in financial software like QuickBooks and Xero.", ["financial software", "QuickBooks", "Xero"]),
    ("Familiar with search engine technologies such as Solr and Elasticsearch.", ["search engine technologies", "Solr", "Elasticsearch"]),
    ("Working knowledge of API testing tools like Postman and SoapUI.", ["API testing tools", "Postman", "SoapUI"]),
    ("Skilled in edge computing and IoT development.", ["edge computing", "IoT development"]),
    ("Proficient in robotics software such as ROS and V-REP.", ["robotics software", "ROS", "V-REP"]),
    ("Experienced in technical writing and API documentation.", ["technical writing", "API documentation"]),
    ("Familiarity with biometric authentication systems and facial recognition.", ["biometric authentication systems", "facial recognition"]),
]

# Process data to format as spaCy model training data
for sentence, skills in TECH_DATA:
    #to handle multiple skills in one sentence make a list
    entities = []
    #same logic as before
    for skill in skills:
        match = re.search(re.escape(skill), sentence, re.IGNORECASE)
        if match:
            start, end = match.span()
            entities.append((start, end, "SKILL"))
    if entities:
        TRAIN_DATA.append((sentence, {"entities": entities}))


# Load a pretrained SpaCy model or create a blank one.
nlp = spacy.load("en_core_web_lg")

# Add or get the Named Entity Recognizer (NER) pipeline component.
if 'ner' not in nlp.pipe_names:
    ner = nlp.add_pipe('ner')
else:
    ner = nlp.get_pipe('ner')

# Add your custom entity labels to the NER component.
for text, annotations in TRAIN_DATA:
    for ent in annotations['entities']:
        if ent[2] not in ner.labels:
            ner.add_label(ent[2]) 

# Disable other pipeline components during training for better performance.
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in ["ner", "transformer"]]
with nlp.disable_pipes(*other_pipes):
    # Initialize the optimizer to start training.
    optimizer = nlp.resume_training()

    # Train your model over multiple epochs, updating it with your training data.
    epochs = 15
    #compounding batch sizes fro accuaracy and speed
    batch_sizes = compounding(8.0, 64.0, 1.001)
    for epoch in range(epochs):
        random.shuffle(TRAIN_DATA)
        losses = {}
        batches = minibatch(TRAIN_DATA, size=batch_sizes)
        for batch in batches:
            examples = []
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                examples.append(example)
            nlp.update(examples, drop=0.5, losses=losses)
        print(f'Epoch trained: {epoch+1}, Losses: {losses}')

# Save the trained model to disk for future use.
nlp.to_disk('resume_model')