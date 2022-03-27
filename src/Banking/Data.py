import pickle

class Data:

    def save_data(data, filename):
        # open the file for writing
        with open(filename + ".data", 'wb') as f:

            # this writes the object a to the
            # file named 'testfile'
            pickle.dump(len(data), f)
            for value in data:
                pickle.dump(value, f)


    def retrieve_data(filename):
        data = []
        try:
            with open(filename + ".data", 'rb') as f:
                for _ in range(pickle.load(f)):
                    data.append(pickle.load(f))
        except FileNotFoundError:
            print("There are no stored " + filename + " to load.")
        return data
