class HelperFunctions:

    def get_string(prompt):
        print(prompt)
        return input()

    def get_next_id(id_list):
        next_id = 1
        for id in id_list:
            if id >= next_id:
                next_id = id+1
        return next_id

    def get_valid_id(id_list, prompt):
        print(prompt)
        id = int(input())
        while id not in id_list and id != 0:
            print("That is not a valid id.  \n" + prompt + "\nOr, enter 0 to cancel and return to the menu.")
            id = int(input())
        return id

