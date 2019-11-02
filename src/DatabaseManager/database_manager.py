from elasticsearch import Elasticsearch

from constants import Constants


class DatabaseManager:
    """
    ElasticSearch database manager
    """
    es = Elasticsearch([{'host': Constants.ES_HOST,
                         'port': Constants.ES_PORT}])

    database = Constants.ES_HOTEL_DATABASE
    doc_type = Constants.ES_HOTEL_DOCTYPE

    request_body = {
        'mappings': {
            'properties': {
                Constants.HOTEL_NAME: {'type': 'text'},
                Constants.HOTEL_ADDRESS: {'type': 'text'},
                Constants.HOTEL_CITY: {'type': 'text'},
                Constants.HOTEL_COUNTRY: {'type': 'text'},
                Constants.HOTEL_LATITUDE: {'type': 'text'},
                Constants.HOTEL_LONGITUDE: {'type': 'text'},
                Constants.HOTEL_POSTAL_CODE: {'type': 'text'},
                Constants.HOTEL_PROVINCE: {'type': 'text'},
                Constants.HOTEL_REVIEWS: {'type': 'text'}
            }}
    }

    # Create if not created
    if not es.indices.exists(Constants.ES_HOTEL_DATABASE):
        es.indices.create(index=Constants.ES_HOTEL_DATABASE
                          , body=request_body)

    @staticmethod
    def add_hotel(doc, _id):
        """
        Add a new hotel document to the database
        :param doc: the doc object
        :param _id: the object id
        """
        DatabaseManager.es.index(index=DatabaseManager.database,
                                 body=doc, id=_id)

    @staticmethod
    def get_hotel(_id):
        """
        Get hotel data by id
        :param _id: the hotel id
        :return:
        """
        hotel_doc = DatabaseManager.es.get(index=DatabaseManager.database,
                                           id=_id)
        return hotel_doc[Constants.ES_DOC_SOURCE]

    @staticmethod
    def clear():
        """
        Clear the hotels database when re-indexing from the dataset file, can be changed later
        to update the current hotel documents.
        """
        if DatabaseManager.es.indices.exists(Constants.ES_HOTEL_DATABASE):
            DatabaseManager.es.indices.delete(Constants.ES_HOTEL_DATABASE)
            DatabaseManager.es.indices.create(index=Constants.ES_HOTEL_DATABASE
                                              , body=DatabaseManager.request_body)
