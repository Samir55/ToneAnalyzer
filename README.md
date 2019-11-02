# Tone Analyzer

API with two endpoints:  

### A. Hotel Indexer (index/)
- A service with one endpoint to get the total emotional tones for a hotel, as described in the next step.
- Calculate the normalized total tones for the hotel using "Watson python lib​".
    - For example, if review #1, for a specific hotel scored 0.25 angry, and 0.80 sad
    - Review #2 scored 0.7 happy, and 0.65 sad
    - Review #3 scored 0.2 happy, 0.7 angry, and 0.4 sad
    - So the total normalized tones for this hotel is 0.47 angry, 0.45 happy, and 0.62
sad.

**Note: in the new api, the tones whose scores are less than 0.7 are removed. so I replace all the tones that have no scores with -1**

### B. Hotel Tone Analyzer (tones/hotel_id)
- Index all hotels data using ElasticSearch
- Each hotel is represented as one document. Each review has its tones scores and the whole
hotel has its normalized tones scores.

# Dataset
Hotels Review dataset on Kaggle
Link: https://www.kaggle.com/datafiniti/hotel-reviews  
**Note** Only 7282_1.csv is downloaded and put in data/downloads

# Dependencies
#### ElasticSearch
you can use [This link](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) for how to download. However if you are on a MacOS device you can install using this command
```console
brew install elastic/tap/elasticsearch-full
```

### Python packages
Run this command
```console
pip3 install -r requirements.txt
```

# Run
1. Start elasticsearch server
```console
elasticsearch
```
2. run this command when you are at the root of the project

```console
python src/main.py
```

to access the 2 endpoints

http://127.0.0.1:5000/index/ --> to run indexing.   
http://127.0.0.1:5000/tones/hotel_id --> to get the normalized tones scores of the hotel with hotel_id.   


Example:
http://127.0.0.1:5000/tones/0 --> to get the normalized tones score for hotel with id 0
