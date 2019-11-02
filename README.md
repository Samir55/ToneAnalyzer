# Tone Analyzer

API with two endpoints:  

### A. Hotel Indexer
- A service with one endpoint to get the total emotional tones for a hotel, as described in the next step.
- Calculate the normalized total tones for the hotel using "Watson python lib​".
    - For example, if review #1, for a specific hotel scored 0.25 angry, and 0.80 sad
    - Review #2 scored 0.7 happy, and 0.65 sad
    - Review #3 scored 0.2 happy, 0.7 angry, and 0.4 sad
    - So the total normalized tones for this hotel is 0.47 angry, 0.45 happy, and 0.62
sad.

### B. Hotel Tone Analyzer
- Index all hotels data using ElasticSearch
- Each hotel is represented as one document. Each review has its tones scores and the whole
hotel has its normalized tones scores.

# Dataset
Hotels Review dataset on Kaggle
Link: https://www.kaggle.com/datafiniti/hotel-reviews  
**Note** Only 7282_1.csv is downloaded and should be put in data/downloads

# Dependencies
####ElasticSearch
you can use [This link](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) for how to download. However if you are on a MacOS device you can install using this command
```console
brew install elastic/tap/elasticsearch-full
```

### Python packages
Run this command
```console
pip3 install -r requirements.txt
```

### Run
After downloading the dataset and copying it to data/7282_1.csv,
run this command when you are at the root of the project

```console
python main.py
```

to access the 2 endpoints

http://127.0.0.1:5000/index/ --> to run indexing
http://127.0.0.1:5000/tones/hotel_id --> to get the normalized tones scores of the hotel with hotel_id
