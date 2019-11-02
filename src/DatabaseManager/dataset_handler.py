import json

import pandas as pd
import numpy as np

from ToneAnalyzer.tone_analyzer import ToneAnalyzer
from constants import Constants


class DatasetHandler:
    """
    Responsible for reading and extracting information from the dataset stored
    as a csv file.
    """

    def __init__(self):
        # Read the dataset
        try:
            dataset = pd.read_csv(Constants.DATASET_PATH)
        except Exception:
            raise Exception('Error reading dataset!')

        # Get the hotels only records
        self.dataset = dataset[dataset.categories.isin(Constants.CATEGORIES)]

        # Get list of hotel names
        self.hotel_names = np.unique(self.dataset[Constants.HOTEL_NAME])

        # Group by hotel names
        self.dataset = self.dataset.groupby(Constants.HOTEL_NAME)

    def get_hotel_data(self, name):
        """
        Get the hotel information from the dataset file and apply tone analyzer on all
        the reviews.

        :param name: Hotel name
        :return: hotel data object
        """
        # Get the hotel data
        hotel_data = self.dataset.get_group(name)

        # Prepare the JSON object
        data = {
            Constants.HOTEL_NAME: str(name),
            Constants.HOTEL_ADDRESS: str(hotel_data[Constants.HOTEL_ADDRESS].iloc[0]),
            Constants.HOTEL_CITY: str(hotel_data[Constants.HOTEL_CITY].iloc[0]),
            Constants.HOTEL_COUNTRY: str(hotel_data[Constants.HOTEL_COUNTRY].iloc[0]),
            Constants.HOTEL_LATITUDE: str(hotel_data[Constants.HOTEL_LATITUDE].iloc[0]),
            Constants.HOTEL_LONGITUDE: str(hotel_data[Constants.HOTEL_LONGITUDE].iloc[0]),
            Constants.HOTEL_POSTAL_CODE: str(hotel_data[Constants.HOTEL_POSTAL_CODE].iloc[0]),
            Constants.HOTEL_PROVINCE: str(hotel_data[Constants.HOTEL_PROVINCE].iloc[0]),
            Constants.HOTEL_REVIEWS: ""}

        # Get the reviews
        reviews = hotel_data[[Constants.HOTEL_REVIEWS_DATE,
                              Constants.HOTEL_REVIEWS_DATE_ADDED,
                              Constants.HOTEL_REVIEWS_DO_RECOMMEND,
                              Constants.HOTEL_REVIEWS_ID,
                              Constants.HOTEL_REVIEWS_RATING,
                              Constants.HOTEL_REVIEWS_TEXT,
                              Constants.HOTEL_REVIEWS_TITLE,
                              Constants.HOTEL_REVIEWS_USER_CITY,
                              Constants.HOTEL_REVIEWS_USER_NAME,
                              Constants.HOTEL_REVIEWS_USER_PROVINCE]]
        # Convert to dict
        reviews = reviews.to_dict(orient='records')

        # Get the tones scores for each review and
        # calculate the hotel normalized tones scores
        tone_analyzer = ToneAnalyzer()

        hotel_normalized_tones = {}
        for tone in Constants.API_TONES_IDS:
            hotel_normalized_tones[tone] = [0., 0.]  # pair representing (Sum of scores , # of tone occurrences)

        for review in reviews:
            # Get the review text and analyze
            review_sentences = str(review[Constants.HOTEL_REVIEWS_TEXT])

            # The api supports only analyzing a single review that is written by one person
            if review_sentences == 'nan' or review_sentences == '':
                review_scores = {}
            else:
                review_scores = tone_analyzer.analyze(review_sentences)

            review[Constants.HOTEL_REVIEWS_TONES] = review_scores

            for tone, score in review_scores.items():
                hotel_normalized_tones[tone][0] += score
                hotel_normalized_tones[tone][1] += 1

        # Normalize the scores
        for tone in Constants.API_TONES_IDS:
            if hotel_normalized_tones[tone][1] <= 0:
                hotel_normalized_tones[tone] = -1
            else:
                hotel_normalized_tones[tone] = hotel_normalized_tones[tone][0] / \
                                               hotel_normalized_tones[tone][1]

        # Add the reviews with their scores and add the hotel total normalized scores
        data[Constants.HOTEL_TONES] = hotel_normalized_tones
        data[Constants.HOTEL_REVIEWS] = json.dumps(reviews)

        # return the document
        return json.dumps(data)
