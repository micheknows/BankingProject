import pickle
import logging


class Data:
    """
    A class to handle saving and retrieving data

    ...

    Attributes
    -----------
    None

    Methods
    ---------
    save_data(data, filename):
        saves the data to the filename

    retrieve_data(filename):
        returns the data retrieved from the filename

    """
    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    def __init__(self):
        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    @staticmethod
    def save_data(data, filename):
        # noinspection GrazieInspection
        """
                saves the data to the filename.data

                Parameters
                -------------
                data    :   List()
                    list of any type of objects

                filename    :   str
                    name of the file to save the data to

                Returns
                -------------
                None

                """
        with open(filename + ".data", 'wb') as f:
            pickle.dump(len(data), f)
            for value in data:
                pickle.dump(value, f)

    @staticmethod
    def retrieve_data(filename):
        """
        returns the data retrieved from filename

        Parameters
        -------------
        filename    :   str
            name of the file to retrieve the data from

        Returns
        -------------
        data    :   List()
            list of objects

        """
        data = []
        try:
            with open(filename + ".data", 'rb') as f:
                for _ in range(pickle.load(f)):
                    data.append(pickle.load(f))
        except FileNotFoundError:
            print("There are no stored " + filename + " to load.")
        return data
