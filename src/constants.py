class Constants:
    ###########################
    # Tone Analyzer API Constants
    ###########################
    API_KEY = 'ga4V4EkbqDUC1AMJmQmNZudDiGBiOGt3MEHWADAIqzgb'
    API_URL = 'https://gateway-lon.watsonplatform.net/tone-analyzer/api'
    API_VERSION = '2017-09-21'

    API_TONES_IDS = ['anger',
                     'fear',
                     'joy',
                     'sadness',
                     'analytical',
                     'confident',
                     'tentative']

    API_FIELD_DOCUMENT_TONE = 'document_tone'
    API_FIELD_TONES = 'tones'
    API_FIELD_TONE_ID = 'tone_id'
    API_FIELD_TONE_SCORE = 'score'

    ###########################
    # Dataset constants
    ###########################
    DATASET_PATH = 'data/7282_1.csv'
    CATEGORIES = ['Hotels']

    HOTEL_ID = '_id'
    HOTEL_NAME = 'name'
    HOTEL_ADDRESS = 'address'
    HOTEL_CITY = 'city'
    HOTEL_COUNTRY = 'country'
    HOTEL_LATITUDE = 'latitude'
    HOTEL_LONGITUDE = 'longitude'
    HOTEL_POSTAL_CODE = 'postalCode'
    HOTEL_PROVINCE = 'province'
    HOTEL_TONES = 'tones'

    HOTEL_REVIEWS = 'reviews'
    HOTEL_REVIEWS_DATE = 'reviews.date'
    HOTEL_REVIEWS_DATE_ADDED = 'reviews.dateAdded'
    HOTEL_REVIEWS_DO_RECOMMEND = 'reviews.doRecommend'
    HOTEL_REVIEWS_ID = 'reviews.id'
    HOTEL_REVIEWS_RATING = 'reviews.rating'
    HOTEL_REVIEWS_TEXT = 'reviews.text'
    HOTEL_REVIEWS_TITLE = 'reviews.title'
    HOTEL_REVIEWS_USER_CITY = 'reviews.userCity'
    HOTEL_REVIEWS_USER_NAME = 'reviews.username'
    HOTEL_REVIEWS_USER_PROVINCE = 'reviews.userProvince'
    HOTEL_REVIEWS_TONES = 'reviews.tones'

    ###########################
    # ElasticSearch Constants
    ###########################
    ES_HOST = 'localhost'
    ES_PORT = 9200

    ES_HOTEL_DATABASE = 'hotels'
    ES_HOTEL_DOCTYPE = 'hotel'
    ES_DOC_SOURCE = '_source'
