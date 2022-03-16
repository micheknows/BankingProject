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
        temp = [account['id'] for account in master_list]
        if temp==None:
            return []
        else:
            return temp
