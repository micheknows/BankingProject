import csv

class ManageVariables:

    def get_next_id(self, id_list):
        if len(id_list) > 0:
            next_id = 1
            for id in id_list:
                if id>=next_id:
                    next_id = next_id + 1
            return next_id
        else:
            return 1


    def get_id_list(self, master_list):
        temp = [account.id for account in master_list]
        if temp==None:
            return []
        else:
            return temp

    def save_variables(self, save_list, filename):
        try:
            with open(filename+".csv", "w") as f:
                writer = csv.writer(f)
                for item in save_list:
                    writer.writerow(item)
        except BaseException as e:
            print("BaseException while saving:  ", filename+".csv")
            print(repr(e))

    def read(self, filename):
        temp = []
        try:
            with open(filename + ".csv", "r") as f:
                csv_reader = csv.reader(f)
                temp_list = [item for item in csv_reader]
                return temp_list
        except BaseException as e:
            print("exception " + repr(e))
        return []

