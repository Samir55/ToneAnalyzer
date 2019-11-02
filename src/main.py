from flask_api import FlaskAPI, status

from DatabaseManager.database_manager import DatabaseManager
from Indexer.indexer import Indexer
from constants import Constants

if __name__ == '__main__':
    # Create app
    app = FlaskAPI(__name__)

    # Database manager
    database_manager = DatabaseManager()


    @app.route('/index/', methods=['GET'])
    def index_hotels():
        try:
            indexer = Indexer(database_manager)
            indexer.index()
            return 'Indexing done', status.HTTP_200_OK
        except Exception:
            return 'Try again later!', status.HTTP_400_BAD_REQUEST


    @app.route('/tones/<int:hotel_id>')
    def get_hotel_tone_scores(hotel_id):
        try:
            data = database_manager.get_hotel(hotel_id)
            return {Constants.API_FIELD_TONES: data[Constants.HOTEL_TONES],
                    Constants.HOTEL_NAME: data[Constants.HOTEL_NAME]}, \
                   status.HTTP_200_OK
        except Exception:
            return 'Not found!', status.HTTP_404_NOT_FOUND


    # Start app
    app.run(debug=True)
