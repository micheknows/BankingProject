class HelperFunctions:

    def get_string(prompt):
        print(prompt)
        return input()

    def get_integer(prompt):
        print(prompt)
        while True:
            try:
                num = int(input())
                return num
            except ValueError:
                print("Please try again.  The entry must be an integer.")

    def get_float(prompt):
        print(prompt)
        while True:
            try:
                num = float(input())
                return num
            except ValueError:
                print("Please try again.  The entry must be a decimal.")

    def get_next_id(id_list):
        next_id = 1
        for id in id_list:
            if id >= next_id:
                next_id = id+1
        return next_id

    def format_currency(num):
        return "{:.2f}".format(num)

    def get_valid_id(id_list, prompt):
        print(prompt)
        id = int(input())
        while id not in id_list and id != 0:
            print("That is not a valid id.  \n" + prompt + "\nOr, enter 0 to cancel and return to the menu.")
            id = int(input())
        return id

    def get_string_from_list(string_list, prompt):
        print(prompt)
        msg = input()
        while msg.lower() not in string_list and msg != "@":
            print("That is not a valid entry.  \n" + prompt + "\nOr, enter @ to cancel and return to the menu.")
            msg = input()
        return msg