from DatabaseManager.dataset_handler import DatasetHandler


class Indexer:
    """
    Responsible for indexing the hotel dataset and adding the hotel docs into
    the database.
    """

    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.id = 0
        pass

    def index(self):
        # Clear the database for re-indexing
        self.db_manager.clear()

        # Create a dataset handler object
        dataset_handler = DatasetHandler()

        # Loop over hotels and add a document for each hotel
        for hotel_name in dataset_handler.hotel_names:
            hotel_doc = dataset_handler.get_hotel_data(hotel_name)

            # Insert the document containing the tones scores into the
            # hotels database
            self.db_manager.add_hotel(hotel_doc, _id=self.id)
            self.id += 1
